from django.urls import path
from .import views
from core.views import single_project
urlpatterns = [
    path('',views.home,name="home"),
    path('single_project/<int:pk>',single_project,name="single_project"),

    

    
]
