from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=150, blank=True)  # اسم الفنان/الشركة
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.display_name or self.user.username

# Create your models here.
