from django.urls import path, include
from . import views

urlpatterns = [
	path('feed_form/',views.feed_form),
	path('allfeeds/',views.all_feeds),
]