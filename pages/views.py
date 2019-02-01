from django.shortcuts import render
from django.contrib import messages

from .forms import EmailForm, PageForm
from .forms import Page

def home(request):
	# print (request.POST['email'])
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_page, created = Page.objects.get_or_created(email=email)
	
	# form = PageForm(request.POST or None)

	# if form.is_valid():
	# 	new_page = form.save(commit = False)
	# 	email = form.cleaned_data['email']
	# 	new_page_old, created= Page.objects.get_or_create(email=email)
		# new_page.save() 

	context = {"form": form}   
	template = "home.html"
	return render(request, template , context)

def about(request):
	return render(request, "about.html", {})

def contact(request):
	return render(request, "contact.html", {})

def testhome(request):
	form = PageForm(request.POST or None)

	if form.is_valid():
		new_page = form.save(commit = False)
		email = form.cleaned_data['email']
		new_page_old, created= Page.objects.get_or_create(email=email)
		if created == True:
			messages.success(request, "Email Was Sucessfully Registered")
		else:
			messages.error(request, "Email is Already Registered")


	context = {"form": form}   
	template = "donotuse.html"
	return render(request, template , context)
