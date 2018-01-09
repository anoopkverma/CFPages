from django.urls import path
from . import views

urlpatterns = [
	path('blog_form/',views.blog_form)
]