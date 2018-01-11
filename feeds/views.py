from django.shortcuts import render, redirect
from .models import Feed
# Create your views here.

def all_feeds(request):
	feeds=Feed.get_feeds()
	content = {'feeds':feeds}
	return render(request,'feeds/allfeeds.html',content)


def feed_form(request):
	if request.method == 'POST' and len(request.POST['post'])>0:
		post = request.POST['post']
		feed = Feed()
		feed.post = post
		feed.user = request.user
		feed.save()
		return allfeeds(request)
	else:
		feeds=Feed.get_feeds()
		content = {'feeds':feeds}
		return render(request,'feeds/feed_form.html',content)

#def comment_form(request):


