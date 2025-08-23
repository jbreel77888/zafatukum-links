from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="البريد الإلكتروني أو اسم المستخدم", max_length=150)
    password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="البريد الإلكتروني", required=True)
    display_name = forms.CharField(label="اسم الفنان أو الشركة", max_length=150, required=True)
    phone = forms.CharField(label="رقم الهاتف", max_length=20, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "display_name", "phone")
