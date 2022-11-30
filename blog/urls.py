from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns=[
	path('', views.blog, name='blog'),
	path('<int:num>/', views.post_details, name='post-details'),	
	path('test/', views.test, name='test'),
	path('author/<str:auth>/', views.blog, name='author'),
	path('category/<str:cat>/', views.blog, name='category'),
	path('search/', views.search, name='search'),


]