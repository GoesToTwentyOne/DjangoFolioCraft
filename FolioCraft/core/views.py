from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from banner_app.models import BannerAppModel
from about_me.models import AboutMeModel,EducationModel,SkillsModel,ProblemSolvedModel
from service_provide.models import ServiceAppModelPart
from accounts.models import Account
from fact_implemented_app.models import FactImplementation
from testimonial.models import TestimonialModel
from showcase.models import ShowcaseModel

# Create your views here.
def home(request):
    banner = get_object_or_404(BannerAppModel)
    about_me=get_object_or_404(AboutMeModel)
    educations=EducationModel.objects.all()
    skills=get_object_or_404(SkillsModel)
    problem_solved=ProblemSolvedModel.objects.all()
    services=ServiceAppModelPart.objects.all() 
    account=get_object_or_404(Account)
    fact_implementations=get_object_or_404(FactImplementation)
    testimonials=TestimonialModel.objects.all()
    projects=ShowcaseModel.objects.all()
    

   
    return render(request,'home.html',context={'banner':banner,'about_me':about_me,'educations':educations,'skills':skills,'problems':problem_solved,'services':services,'account':account,'fact_implementations':fact_implementations,'testimonials':testimonials,'projects':projects,'accounts':account})

def single_project(request,pk):
    single_project = ShowcaseModel.objects.get(pk=pk)
    banner = get_object_or_404(BannerAppModel)
    account=get_object_or_404(Account)
    return render(request,'portfolio-single.html',context={'single_project':single_project,'banner':banner,'account':account})



    