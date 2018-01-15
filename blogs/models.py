from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=255, null=False, unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=2000)
	create_date = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	content = models.TextField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey(
		'Comment',
		null=True, 
		blank=True, 
		on_delete=models.CASCADE)

	def __str__(self):
		return self.content





