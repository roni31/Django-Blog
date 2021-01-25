from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from django.core.paginator import Paginator
from .forms import BlogForm

def index(request):
	# return HttpResponse("Hello World")
	q = Blog.objects.all()
	p = Paginator(q,2) # 1 record per page
	try:
		page_number = request.GET.get('page') # For pagination
		page_object = p.page(page_number)
	except:
		page_object = p.page(2)

	return render(request, 'index.html', {'page_object':page_object}) # context

def login(request):
	return render(request, 'login.html', {})

def addblog(request):
	form = BlogForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, 'addblog.html', {'form':form})

def home(request):
	return render(request, 'home.html', {})
