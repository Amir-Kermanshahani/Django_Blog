from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
	return render(request, 'web/index.html')


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