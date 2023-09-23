from django.db import models
from accounts.models import Account

# Create your models here.
class TestimonialModel(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="testimonials")
    photo=models.ImageField(upload_to='images/testimonials',null=True)
    quote=models.TextField()
    name=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    class Meta:
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'
    def __str__(self):
        return self.user.username