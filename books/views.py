from django.shortcuts import render
# from django.views.generic import View
from django.views import View


# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "home.html", context)