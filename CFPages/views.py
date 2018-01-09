from django.shortcuts import render
from blogs.models import Blog

def home(request):
	blogs=Blog.objects.all().order_by('-create_date')
	content = {'blogs':blogs}
	return render(request, 'home.html', content)