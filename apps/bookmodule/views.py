from django.http import HttpResponse
from django.shortcuts import render

from .models import Book
from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Address, Student
from .forms import BookForm

from django.db.models import Count
from .models import Address
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm
from django.shortcuts import render
from django.db.models import Sum
from .models import Book


from django.shortcuts import render
from django.db.models import Sum
from .models import Book

from django.shortcuts import render
from django.db.models import Sum
from .models import Publisher
from django.db.models import Sum
from .models import Publisher

def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/lab9/task6.html', {'publishers': publishers})


def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9/task5.html', {'publishers': publishers})

def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9/task4.html', {'publishers': publishers})


def lab9_task3(request):
    publishers = Publisher.objects.all()
    result = []

    for pub in publishers:
        oldest_book = pub.book_set.order_by('pubdate').first()
        result.append({
            'publisher': pub,
            'oldest_book': oldest_book
        })

    return render(request, 'bookmodule/lab9/task3.html', {'result': result})



def lab9_task2(request):
    publishers = Publisher.objects.annotate(
        total_book_stock=Sum('book__quantity')
    )
    return render(request, 'bookmodule/lab9/task2.html', {'publishers': publishers})

def lab9_task1(request):
    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 0
    books = Book.objects.all()

    for book in books:
        if total_quantity > 0:
            book.percentage = (book.quantity / total_quantity) * 100
        else:
            book.percentage = 0

    return render(request, 'bookmodule/lab9/task1.html', {'books': books})



def lab8_task7(request):
    cities = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'cities': cities})


def lab8_task5(request):
    stats = Book.objects.aggregate(
        count_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})



def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=2) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})


def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def __getBooksList():
    book1 = {
        'id': 12344321,
        'title': 'Continuous Delivery',
        'author': 'J.Humble and D. Farley'
    }
    book2 = {
        'id': 56788765,
        'title': 'Reversing: Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }
    book3 = {
        'id': 43211234,
        'title': 'The Hundred-Page Machine Learning Book',
        'author': 'Andriy Burkov'
    }
    return [book1, book2, book3]


def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, "bookmodule/search.html")




def html5_tables(request):
    return render(request, "bookmodule/html5_tables.html")

def html5_listing(request):
    return render(request, "bookmodule/html5_listing.html")

def html5_text_formatting(request):
    return render(request, "bookmodule/html5_text_formatting.html")

def html5_links(request):
    return render(request, "bookmodule/html5_links.html")

def index(request):
    return render(request, "bookmodule/index.html")

def listbooks(request):
    return render(request, "bookmodule/listbooks.html")

def onebook(request, bookId):
    return render(request, "bookmodule/onebook.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})



def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    book1 = {
        'id': 123,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley'
    }
    book2 = {
        'id': 456,
        'title': 'Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    return render(request, 'bookmodule/show.html', {'book': targetBook})
