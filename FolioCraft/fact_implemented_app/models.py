from django.db import models
from accounts.models import Account
# Create your models here.
class FactImplementation(models.Model):
    user =models.OneToOneField(Account, on_delete=models.CASCADE,related_name="fact_implementation")
    feature_items=models.IntegerField()
    active_products=models.IntegerField()
    year_experiences=models.IntegerField()
    our_clinets=models.IntegerField()
    class Meta:
        verbose_name = 'fact_implementation'
        verbose_name_plural = 'fact_implementations'
    def __str__(self):
        return self.user.username
    