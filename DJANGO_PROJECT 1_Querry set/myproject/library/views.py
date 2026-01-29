# Create your views here.
from django.shortcuts import render
from .models import Book
from django.db.models import Q  # Import Q expressions for OR / AND filters

def book_list(request):
    # 1. Get all books
    all_books = Book.objects.all()  # Returns all Book objects as QuerySet

    # 2. Return specific columns using values()
    books_values = Book.objects.values('title', 'author')
    # Returns a list of dictionaries: [{'title':'Book1', 'author':'Author1'}, ...]

    # 3. Return specific columns as tuples using values_list()
    books_values_list = Book.objects.values_list('title', 'price')
    # Returns list of tuples: [('Book1', 20.5), ('Book2', 15.0)]

    # 4. Filter specific rows using filter() method
    books_by_author = Book.objects.filter(author='J.K. Rowling')
    # Returns all books where author matches exactly

    # 5. Filter using Q expressions and OR '|'
    books_q = Book.objects.filter(Q(price__lt=30) | Q(author='J.R.R. Tolkien'))
    # Books cheaper than 30 OR by Tolkien

    # 6. Field lookups (exact, contains, icontains, gt, lt, etc.)
    books_title_contains = Book.objects.filter(title__icontains='harry')
    # 'icontains' = case-insensitive substring match

    # 7. Order by ascending
    books_ordered_asc = Book.objects.order_by('price')  # Lowest price first

    # 8. Order by descending
    books_ordered_desc = Book.objects.order_by('-price')  # Highest price first

    # 9. Multiple order by: first by author ascending, then price descending
    books_multi_order = Book.objects.order_by('author', '-price')

    # Pass all QuerySets to template
    context = {
        'all_books': all_books,
        'books_values': books_values,
        'books_values_list': books_values_list,
        'books_by_author': books_by_author,
        'books_q': books_q,
        'books_title_contains': books_title_contains,
        'books_ordered_asc': books_ordered_asc,
        'books_ordered_desc': books_ordered_desc,
        'books_multi_order': books_multi_order,
    }

    return render(request, 'library/book_list.html', context)