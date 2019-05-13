from django.shortcuts import render
from .models import Book
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


def search_view(request):
	books = Book.objects.all()
	context = {
		'books': books,
	}
	return render(request,"search.html",context)