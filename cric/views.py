from django.shortcuts import render,redirect
from .models import india,Australia,South_Africa,England
from django.views.generic.detail import DetailView
from django.contrib.auth import(
	login,
	logout,
	authenticate,
	get_user_model,
	)
from . forms import userloginform,newuserform


def index(request):
	return render(request, "index.html")

def india_v(request):
	rec_posts1 = india.objects.order_by('-Date_of_Publishing')[0:1]
	rec_posts2 = india.objects.order_by('-Date_of_Publishing')[1:2]
	rec_posts3 = india.objects.order_by('-Date_of_Publishing')[2:3]
	post = india.objects.all()
	context = {'rec_posts1':rec_posts1,'rec_posts2':rec_posts2,'rec_posts3':rec_posts3,'post':post}
	return render(request,"india.html",context)

def australia_v(request):
	rec_posts1 = Australia.objects.order_by('-Date_of_Publishing')[0:1]
	rec_posts2 = Australia.objects.order_by('-Date_of_Publishing')[1:2]
	rec_posts3 = Australia.objects.order_by('-Date_of_Publishing')[2:3]
	post = Australia.objects.all()
	context = {'rec_posts1':rec_posts1,'rec_posts2':rec_posts2,'rec_posts3':rec_posts3,'post':post}
	return render(request,"aus.html",context)

def south_africa_v(request):
	rec_posts1 = South_Africa.objects.order_by('-Date_of_Publishing')[0:1]
	rec_posts2 = South_Africa.objects.order_by('-Date_of_Publishing')[1:2]
	rec_posts3 = South_Africa.objects.order_by('-Date_of_Publishing')[2:3]
	post = South_Africa.objects.all()
	context = {'rec_posts1':rec_posts1,'rec_posts2':rec_posts2,'rec_posts3':rec_posts3,'post':post}
	return render(request,"sa.html",context)

def england_v(request):
	rec_posts1 = England.objects.order_by('-Date_of_Publishing')[0:1]
	rec_posts2 = England.objects.order_by('-Date_of_Publishing')[1:2]
	rec_posts3 = England.objects.order_by('-Date_of_Publishing')[2:3]
	post = England.objects.all()
	context = {'rec_posts1':rec_posts1,'rec_posts2':rec_posts2,'rec_posts3':rec_posts3,'post':post}
	return render(request,"eng.html",context)

class indiaDetailView(DetailView):

	model = india

	def get_context_data(self, **kwargs):
		context = super(indiaDetailView, self).get_context_data(**kwargs)
		return context

class australiaDetailView(DetailView):

	model = Australia

	def get_context_data(self, **kwargs):
		context = super(australiaDetailView, self).get_context_data(**kwargs)
		return context

class south_africaDetailView(DetailView):

	model = South_Africa

	def get_context_data(self, **kwargs):
		context = super(south_africaDetailView, self).get_context_data(**kwargs)
		return context

class englandDetailView(DetailView):

	model = England

	def get_context_data(self, **kwargs):
		context = super(englandDetailView, self).get_context_data(**kwargs)
		return context

def userlogin(request):
	title ="User Login"
	form = userloginform(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		newuser = authenticate(username=username,password=password)
		login(request,newuser)
		return redirect('/admin')
	return redirect('/admin')

def newuser(request):
	title="User Registration"
	signup=newuserform(request.POST)
	if signup.is_valid():
		user=signup.save(commit=False)
		password=signup.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)
		return redirect('/')
	return render(request,"index.html",{"signup":signup,"title":title})
