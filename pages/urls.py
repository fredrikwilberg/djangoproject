from django.urls import path
from . import views

urlpatterns = [
	path('', views.testhome, name ='testhome'),
	path('about/', views.about, name ='about'),
	path('contact/', views.contact, name ='contact'),
	path('testhome/', views.testhome, name ='home')



]  