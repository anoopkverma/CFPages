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
		return all_feeds(request)
	else:
		feeds=Feed.get_feeds()
		content = {'feeds':feeds}
		return render(request,'feeds/feed_form.html',content)


def feed_view(request,feed_id):
	feed = Feed.objects.get(id=feed_id)
	if request.method=="POST":
		content = request.POST['content']
		comment =  Feed()
		comment.content =  content
		comment.user = request.user
		comment.parent = feed
		comment.save()
	comments = Feed.objects.filter(parent=feed)
	return render(request,'feeds/feed.html',{'feed':feed, 'comments':comments})



