from django.shortcuts import render
from .models import Book
# Create your views here.
def book_view(request):
	if(Book.objects.first()):
		book = Book.objects.first().content_pdf
		context = {
			'x': book,
		}
		return render(request,"index.html",context)
	return render(request,"index.html",{})
	# print(User.objects.get(id=id))