from django.shortcuts import render
# from django.views.generic import View
from django.views import View


# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "home.html", context)
from .models import Book
from django.views.generic.list import ListView 
# Create your views here.
def book_view(request,id):
	book = Book.objects.get(id=id)
	# if(Book.objects.first()):
		# book = Book.objects.last()
		# print(help(book))
	context = {
		'x': book,
	}
	return render(request,"index.html",context)
	# return render(request,"index.html",{})
	# print(User.objects.get(id=id))

class SearchView(ListView):
	template_name = 'search.html'
	# queryset = Book.objects.all()
	def get_queryset(self,*args,**kwargs):
		qs = Book.objects.all()
		# print(self.request.GET['q'])
		query = self.request.GET.get('q',None)
		if query:
			qs = qs.filter(name__icontains=query)
		return qs 
	def get_context_data(self,*args,**kwargs):
		context = super(SearchView,self).get_context_data(*args,**kwargs)
		# context['books'] = Book.objects.all()
		return context
# def search_view(request):
# 	books = Book.objects.all()
# 	context = {
# 		'books': books,
# 	}
# 	return render(request,"search.html",context)
