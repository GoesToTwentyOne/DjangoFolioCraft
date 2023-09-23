from django.shortcuts import render,HttpResponse,get_object_or_404
from banner_app.models import BannerAppModel
from about_me.models import AboutMeModel,EducationModel,SkillsModel,ProblemSolvedModel
from service_provide.models import ServiceAppModelPart
from accounts.models import Account

# Create your views here.
def home(request):
    banner = get_object_or_404(BannerAppModel)
    about_me=get_object_or_404(AboutMeModel)
    educations=EducationModel.objects.all()
    skills=get_object_or_404(SkillsModel)
    problem_solved=ProblemSolvedModel.objects.all()
    services=ServiceAppModelPart.objects.all() 
    account=get_object_or_404(Account)
    return render(request,'home.html',context={'banner':banner,'about_me':about_me,'educations':educations,'skills':skills,'problems':problem_solved,'services':services,'account':account})

