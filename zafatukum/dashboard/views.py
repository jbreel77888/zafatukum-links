from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Release, Earnings, Activity

@login_required
def home(request):
    # بيانات الإحصائيات
    stats = {
        "total_earnings": 12847,
        "total_streams": 2400000,
        "active_releases": 47,
        "monthly_revenue": 3249,
        "monthly_change": -2.1  # أو +2.5
    }

    # آخر النشاطات
    activities = Activity.objects.filter(release__artist__id=1).order_by('-timestamp')[:5]

    # الإصدارات
    releases = Release.objects.all().order_by('-upload_date')

    context = {
        "stats": stats,
        "activities": activities,
        "releases": releases,
    }
    return render(request, "dashboard/home.html", context)

