from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
from .models import Book, Publisher, Author


from django.shortcuts import render
from django.db.models import Sum
from .models import Book
from .forms import BookForm

from django.shortcuts import render
from django.db.models import Sum
from .models import Publisher
from django.db.models import Sum
from .models import Publisher
from .models import Student2, Address2
from .forms import Student2Form, Address2Form

from .models import Student, Address
from .forms import StudentForm, AddressForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Address, Student2, Address2, StudentImage
from .forms import StudentForm, Student2Form, StudentImageForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

def registerUser(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'You have successfully registered')

            return redirect('/users/login/')

        else:
            messages.error(request, 'Registration error. Please check the form.')

    context = {'form': form}

    return render(request, 'bookmodule/register.html', context)


# Task 1: One address for each student
@login_required(login_url='/users/login/')
def lab11_list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab11/list_students.html', {'students': students})

@login_required(login_url='/users/login/')
def lab11_add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:lab11_list_students')
    else:
        form = StudentForm()

    return render(request, 'bookmodule/lab11/add_student.html', {'form': form})

@login_required(login_url='/users/login/')
def lab11_edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('books:lab11_list_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'bookmodule/lab11/edit_student.html', {'form': form})

@login_required(login_url='/users/login/')
def lab11_delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('books:lab11_list_students')


# Task 2: Many-to-many addresses
@login_required(login_url='/users/login/')
def lab11_list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/lab11/list_students2.html', {'students': students})

@login_required(login_url='/users/login/')
def lab11_add_student2(request):
    if request.method == "POST":
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:lab11_list_students2')
    else:
        form = Student2Form()

    return render(request, 'bookmodule/lab11/add_student2.html', {'form': form})

@login_required(login_url='/users/login/')
def lab11_edit_student2(request, id):
    student = get_object_or_404(Student2, id=id)

    if request.method == "POST":
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('books:lab11_list_students2')
    else:
        form = Student2Form(instance=student)

    return render(request, 'bookmodule/lab11/edit_student2.html', {'form': form})

@login_required(login_url='/users/login/')
def lab11_delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('books:lab11_list_students2')


# Task 3: Image handling
@login_required
def lab11_list_images(request):
    students = StudentImage.objects.all()
    return render(request, 'bookmodule/lab11/list_images.html', {'students': students})

@login_required
def lab11_add_image(request):
    if request.method == "POST":
        form = StudentImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:lab11_list_images')
    else:
        form = StudentImageForm()

    return render(request, 'bookmodule/lab11/add_image.html', {'form': form})

@login_required
def lab11_delete_image(request, id):
    student = get_object_or_404(StudentImage, id=id)
    student.delete()
    return redirect('books:lab11_list_images')







def lab10_part2_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:lab10_part2_listbooks')


def lab10_part2_editbook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:lab10_part2_listbooks')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/lab10_part2/editbook.html', {'form': form})

def lab10_part2_addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.pubdate = timezone.now()  
            book.save()
            form.save_m2m()
            return redirect('books:lab10_part2_listbooks')
    else:
        form = BookForm()

    return render(request, 'bookmodule/lab10_part2/addbook.html', {'form': form})

def lab10_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part2/listbooks.html', {'books': books})

def lab10_part1_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:lab10_part1_listbooks')

def lab10_part1_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    publishers = Publisher.objects.all()
    authors = Author.objects.all()

    if request.method == "POST":
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.rating = request.POST.get('rating')
        book.publisher_id = request.POST.get('publisher')
        book.save()

        book.authors.set(request.POST.getlist('authors'))

        return redirect('books:lab10_part1_listbooks')

    return render(request, 'bookmodule/lab10_part1/editbook.html', {
        'book': book,
        'publishers': publishers,
        'authors': authors
    })


def lab10_part1_addbook(request):
    publishers = Publisher.objects.all()
    authors = Author.objects.all()

    if request.method == "POST":
        book = Book.objects.create(
            title=request.POST.get('title'),
            price=request.POST.get('price'),
            quantity=request.POST.get('quantity'),
            pubdate=timezone.now(),
            rating=request.POST.get('rating'),
            publisher_id=request.POST.get('publisher')
        )

        book.authors.set(request.POST.getlist('authors'))

        return redirect('books:lab10_part1_listbooks')

    return render(request, 'bookmodule/lab10_part1/addbook.html', {
        'publishers': publishers,
        'authors': authors
    })


def lab10_part1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part1/listbooks.html', {'books': books})



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
