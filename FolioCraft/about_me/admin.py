from django.contrib import admin
from about_me.models import AboutMeModel,EducationModel,SkillsModel,ProblemSolvedModel

# Register your models here.
admin.site.register(AboutMeModel)
admin.site.register(EducationModel)
admin.site.register(SkillsModel)
admin.site.register(ProblemSolvedModel)
