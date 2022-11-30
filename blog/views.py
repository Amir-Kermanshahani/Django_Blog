from django.shortcuts import render

# Create your views here.
from email import message
from telnetlib import STATUS
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment, Category
from web.models import Contact
from blog.forms import CForm, CommentForm
from taggit.models import Tag

# Create your views here.
def blog(request, **kwargs):
	categories = Category.objects.all()
	#tags = Tag.objects,all()
	posts = Post.objects.all()
	posts = Post.objects.filter(Active=1)
	if kwargs.get('auth'):
		posts = posts.objects.filter(author=kwargs['auth'])
	if kwargs.get('cat'):
		posts = posts.filter(category=kwargs['cat'])
	context = {'posts':posts, 'categories':categories}
	return render(request, 'blog/blog.html', context)

def post_details(request, num):
	if request.method == 'POST':
		forms = CommentForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('/blog/')
		
	posts = Post.objects.filter(Active=1, pk=num)
	post = get_object_or_404(posts)
	comments = Comment.objects.filter(status=1, post=posts.id)
	forms =  CommentForm()
	context = {'posts':posts, 'comments':comments, 'forms':forms, 'post':post}
	return render(request, 'blog/post-details.html', context)

def test(request):
	if request.method == 'POST':
		forms = test(request.POST)
		if forms.is_valid:
			name = forms.cleaned_data['name']
			email = forms.cleaned_data['email']
			subject = forms.cleaned_data['subject']
			message = forms.cleaned_data['message']
			f = Contact()
			f.name = name
			f.email = email
			f.subject = subject
			f.message = message
			f.save()
			return redirect('/')
		
		return render(request, 'blog/test.html')

def search(request):
	posts = Post.objects.all.filter(Active=1)
	if request.method == 'GET':
		search = request.GET.get('s')
		posts = posts.filter(content__contains = search)
	context = {'posts':posts}
	return render(request, 'blog/test.html', context)
