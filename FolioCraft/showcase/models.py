from django.db import models
from accounts.models import Account
# Create your models here.
class ShowcaseModel(models.Model):
    user=models.ForeignKey(Account, on_delete=models.CASCADE,related_name='showcase')
    name=models.CharField(max_length=200,null=True)
    profile_photo=models.ImageField(upload_to='images/projects')
    creators_review=models.CharField(max_length=100)
    project_showcase_image=models.ImageField(upload_to='images/projects/showcase')
    single_project_page_image=models.ImageField(upload_to='images/projects/single_project')
    category_type=models.CharField(max_length=200)
    project_tittle_showcase=models.CharField(max_length=15)
    project_tittle_single_project_page=models.CharField(max_length=250)
    project_description=models.TextField()
    class Meta:
         verbose_name="Showcase"
         verbose_name_plural="Showcases"
    def __str__(self):
        return self.user.username