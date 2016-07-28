from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class Home(View):
	template_name = "cafe/home.html"

	def get(self,request):
		return render(request,self.template_name)

class Menu(View):
	template_name = "cafe/menu.html"

	def get(self,request):
		return render(request,self.template_name)

class About(View):
	template_name = "cafe/about.html"

	def get(self,request):
		return render(request,self.template_name)

class Contact(View):
	template_name = "cafe/contact.html"

	def get(self,request):
		return render(request,self.template_name)