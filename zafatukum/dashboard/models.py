from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Release(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    status_choices = [
        ('pending', 'قيد المراجعة'),
        ('review', 'تحت المراجعة'),
        ('sent', 'تم الإرسال'),
        ('rejected', 'مرفوض'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    platforms = models.CharField(max_length=200, default="Spotify, Apple Music, YouTube")

    def __str__(self):
        return self.title

class Earnings(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Activity(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
