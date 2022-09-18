from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm
from comments.forms import CommentForm
from .utils import searchBooks, paginateBooks
from django.contrib.auth.decorators import login_required

# @login_required(login_url="login")
def books(request):
    books, search_query = searchBooks(request)
    custom_range, books = paginateBooks(request, books, 6)

    context = {'books': books,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'books/books.html', context)

# @login_required(login_url="login")
def book(request, pk):
    bookObj = Book.objects.get(id=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.book = bookObj
        comment.user = request.user.profile
        comment.save()

        messages.success(request, 'Your comment was successfully submitted!')
        return redirect('book', pk=bookObj.id)

    return render(request, 'books/single-book.html', {'book': bookObj,'form': form})

@login_required(login_url="login")
def createBook(request):
    profile = request.user.profile
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = profile
            book.save()

            return redirect('books')

    context = {'form': form}
    return render(request, "books/book_form.html", context)

@login_required(login_url="login")
def updateBook(request, pk):
    profile = request.user.profile
    book = profile.book_set.get(id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('books')

    context = {'form': form}
    return render(request, "books/book_form.html", context)


@login_required(login_url="login")
def deleteBook(request, pk):
    profile = request.user.profile
    book = profile.book_set.get(id=pk)
    if book:
        if request.method == 'POST':
            book.delete()
            return redirect('books')


    context = {'object': book}
    return render(request, 'delete_template.html', context)
