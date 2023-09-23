from django.db import models
from django.urls import reverse
from accounts.models import Account

# Create your models here.
class BannerAppModel(models.Model):
    user= models.OneToOneField(Account, on_delete=models.CASCADE,related_name='banner')
    moto_heading = models.TextField()
    pro_file_image = models.ImageField(upload_to='images/banners', blank=True)
    linkedin_profile_link=models.TextField(blank=True)
    Skype_profile_link=models.TextField(blank=True)
    twitter_profile_link=models.TextField(blank=True)
    facebook_profile_link=models.TextField(blank=True)
    instagram_link=models.TextField(blank=True)
    discord_profile_link=models.TextField(blank=True)

    class Meta:
        verbose_name = 'banner_app'
        verbose_name_plural = 'banners'
    def __str__(self):
        return self.user.username
