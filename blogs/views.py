from django.shortcuts import render
from .models import Blog, Comment
from CFPages.views import home
from users.views import login_view
# Create your views here.

def blog_form(request):
	if not request.user.is_authenticated:
		return login_view(request)
	if request.method == 'POST' and validate_blog_form(request.POST):
		title = request.POST['title']
		content = request.POST['content']
		blog = Blog()
		blog.title = title
		blog.content = content
		blog.user = request.user
		blog.save()
		return home(request)
	else:
		return render(request,'blogs/blog_form.html')


def validate_blog_form(blog):
	flag = False
	if len(blog['title']) > 0 and len(blog['content']) > 0:
		flag = True
	return flag

def blog(request,blog_id):
	blog = Blog.objects.get(id=blog_id)
	if request.method=="POST":
		content = request.POST['comment']
		comment =  Comment()
		comment.content =  content
		comment.user = request.user
		comment.blog = blog
		comment.save()
	comments = Comment.objects.filter(blog=blog)
	return render(request,'blogs/blog.html',{'blog':blog, 'comments':comments})

def my_blogs(request):
	blogs = Blog.objects.filter(user=request.user).order_by('-create_date')
	content = {'blogs':blogs}
	return render(request, 'home.html', content)