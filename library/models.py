from django.db import models
from user_auth.models import OurUser

# Create your models here.


class AuthCode(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # auth_users = ?
    # main_url = models.CharField(max_length=250)
    docs_url = models.CharField(max_length=500)
    num_comments = models.IntegerField(verbose_name='Comments', default=0)
    num_likes = models.IntegerField(verbose_name='Likes', default=0)
    num_dislikes = models.IntegerField(verbose_name='Dislikes', default=0)
    num_downloads = models.IntegerField(verbose_name='Downloads', default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(
        OurUser, related_name='Commenter', on_delete=models.CASCADE)
    auth_code = models.ForeignKey(AuthCode, on_delete=models.CASCADE)
    comment = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Notification(models.Model):
    notification_types = (
        ('welcome', 'Welcome'),
        ('new_upload', 'New Upload'),
        ('profile_update', 'Profile Update'),
        ('password_reset', 'Password Reset'),
    )

    user = models.ForeignKey(
        OurUser, related_name='Owner', on_delete=models.CASCADE)
    notification = models.TextField(blank=True, null=True)
    notification_type = models.CharField(
        max_length=20, choices=notification_types, default='welcome')
    seen = models.BooleanField(verbose_name='Read', default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification
