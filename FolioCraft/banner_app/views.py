from django.shortcuts import render
from banner_app.models import BannerAppModel

# Create your views here.
def bannerView(request):
    banner = BannerAppModel.objects.all()
    print(banner)
    return render(request,'home.html',context={'banner':banner})