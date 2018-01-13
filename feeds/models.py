from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Feed(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey(
		'Feed',
		null=True, 
		blank=True, 
		on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)


	def __str__(self):
		return self.content

	@staticmethod
	def get_feeds():
		feed = Feed.objects.filter(parent=None).order_by('-date')
		return feed

	@staticmethod
	def get_comments():
		comments = Feed.objects.filter(parent=self).order_by(date)
		return comments


