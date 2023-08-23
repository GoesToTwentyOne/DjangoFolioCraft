from django.urls import path
from banner_app.views import bannerView
urlpatterns = [
    path('',bannerView,name="banner")
]

