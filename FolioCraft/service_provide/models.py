from django.db import models
from accounts.models import Account

# Create your models here.
class ServiceAppModelPart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='services', default=1)
    bullet_class=models.CharField(max_length=150)
    service_title=models.CharField(max_length=200)
    service_short_description=models.CharField(max_length=300)
    class Meta:
        verbose_name="Service"
        verbose_name_plural="Services"
    def __str__(self):
        return self.user.username