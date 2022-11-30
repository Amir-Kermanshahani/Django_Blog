from django.urls import path
from web import views

app_name = 'web'

urlpatterns=[
	path('', views.index, name='index'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about')

]