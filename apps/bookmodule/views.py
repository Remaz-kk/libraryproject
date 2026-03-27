from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render


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
