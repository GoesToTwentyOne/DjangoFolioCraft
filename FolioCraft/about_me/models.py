from django.db import models
from accounts.models import Account

# Create your models here.
from django.db import models
from accounts.models import Account

class AboutMeModel(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='about_me')
    about_your_self = models.TextField()
    class Meta:
        verbose_name = 'about_your_self'
        verbose_name_plural = 'Abouts'
    def __str__(self):
        return self.user.username

class EducationModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='educations')
    title = models.CharField(max_length=200)
    beginning_year = models.IntegerField()
    end_year = models.IntegerField()
    percentage_completed = models.IntegerField()
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
    def __str__(self):
        return self.user.username

class SkillsModel(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='skills')
    proficient = models.TextField(blank=True)
    comfortable = models.TextField(blank=True)
    familiar = models.TextField(blank=True)
    tools = models.TextField(blank=True)
    concepts = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    def __str__(self):
        return self.user.username

class ProblemSolvedModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='problems_solved')
    judge_name = models.CharField(max_length=200)
    total_solved = models.IntegerField()
    links = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Problem Solve'
        verbose_name_plural = 'Solves'
    def __str__(self):
        return self.user.username

 