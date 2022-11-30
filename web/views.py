from django.shortcuts import render, redirect
from .forms import ContactForm
from blog.models import Post, Category


def index(request):

	categories = Category.objects.all()
	posts = Post.objects.all()
	posts = Post.objects.filter(Active=1)
	posts = Post.objects.order_by('-created_time')[:6]

	return render(request, 'web/index.html', {'recent_posts':posts, 'categories':categories})


def contact(request):
	if request.method == 'POST':
		forms = ContactForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('/')
	forms = ContactForm()
	return render(request, 'web/contact.html', {'forms':forms})

def about(request):
	return render(request, 'web/about.html')