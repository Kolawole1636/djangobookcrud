from django.shortcuts import render, redirect

# Create your views here.
from .models import Book


def home(request):

    if request.method == 'POST':

        book_name = request.POST['bookname']
        book_author = request.POST['author']
        book_pages = request.POST['page']

        new_book = Book(name=book_name, author=book_author, pages= book_pages)
        new_book.save()

        return redirect('books')



    return render(request, "home.html")


def all_books(request):

    books = Book.objects.all()

    return render(request, "book.html", context={"all_books" : books})




def remove_book(request, pk):

     book_to_delete = Book.objects.get(id=pk)

     book_to_delete.delete()

     return redirect('books')




def edit_book(request, pk):

    book_to_edit = Book.objects.get(id=pk)

    return render(request, 'edit.html', context={"bookedit": book_to_edit})





def update_book(request, pk):

    book_to_update = Book.objects.get(id=pk)

    if request.method == 'POST':

        book_to_update.name = request.POST['bookname']
        book_to_update.author = request.POST['author']
        book_to_update.pages = request.POST['page']

        book_to_update.save()

        return redirect('books')




















