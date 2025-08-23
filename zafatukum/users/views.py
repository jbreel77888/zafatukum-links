from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm
from .models import Profile

def _get_username_from_input(value: str) -> str:
    # يسمح بتسجيل الدخول عبر البريد أو اسم المستخدم
    if '@' in value:
        try:
            user = User.objects.get(email__iexact=value)
            return user.username
        except User.DoesNotExist:
            return value
    return value

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username_input = form.cleaned_data["username_or_email"]
        password = form.cleaned_data["password"]
        username = _get_username_from_input(username_input)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, "بيانات الدخول غير صحيحة.")
    return render(request, "users/login.html", {"form": form, "tab": "login"})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.email = form.cleaned_data["email"]
        user.save()
        # أنشئ/حدث الملف الشخصي
        Profile.objects.update_or_create(
            user=user,
            defaults={
                "display_name": form.cleaned_data.get("display_name", ""),
                "phone": form.cleaned_data.get("phone", ""),
            }
        )
        login(request, user)
        messages.success(request, "تم إنشاء الحساب بنجاح!")
        return redirect('home')
    return render(request, "users/register.html", {"form": form, "tab": "register"})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    # صفحة بسيطة لاختبار الدخول — لاحقًا سنستبدلها بالداشبورد
    profile = getattr(request.user, 'profile', None)
    return render(request, "users/home.html", {"profile": profile})

# Create your views here.
