from django.urls import path
from . import views

urlpatterns = [
	path('blog_form/', views.blog_form),
	path('<int:blog_id>/', views.blog),
	path('my_blogs/', views.my_blogs),
]