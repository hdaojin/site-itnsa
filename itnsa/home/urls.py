from django.urls import path

from . import views

# create your urls here

app_name = 'home'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
]
