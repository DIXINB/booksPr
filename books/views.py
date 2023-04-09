from django.shortcuts import get_object_or_404, render
from django.http import FileResponse
import os
from books.models import Book # импорт модели Book из файла books/models.py
from books.models import Author
from books.models import Hist
from books.models import Artc
from books.models import Dict
from books.models import Pros
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#def index(request):
#    book_list = Book.objects.all().order_by('id')
#    return render(request, "hpage/index2.html", {"book_list": book_list})
	
	
def view(request, id):
    b = get_object_or_404(Book, id=id)
    return render(request, "view.html", {"Book": b})
def my_homepage(request):
    #book_list = Book.objects.all().order_by('id')
    return render(request, "books/my_homepage.html")
def mail(request):
    return render(request, "books/mail_repair.html")
def forum(request):
    return render(request, "books/forum_repair.html")	
def history(request):
    hist_list = Hist.objects.all()
       
    page = request.GET.get('page', 1)
    paginator = Paginator(hist_list, 7)
    try:
        hist_list = paginator.page(page)
    except PageNotAnInteger:
        hist_list = paginator.page(1)
    except EmptyPage:
        hist_list = paginator.page(paginator.num_pages)
    
    return render(request, "books/history.html",{"hist_list": hist_list})	

def history1(request):
    h1 = Hist.objects.get(ind='1')
    return render(request, "books/history1.html", {"h1": h1})
def history2(request):
    h2 = Hist.objects.get(ind='2')
    return render(request, "books/history2.html", {"h2": h2})
def history3(request):
    h3 = Hist.objects.get(ind='3')
    return render(request, "books/history3.html", {"h3": h3})
def history4(request):
    h4 = Hist.objects.get(ind='4')
    return render(request, "books/history4.html", {"h4": h4})	
def history5(request):
    h5 = Hist.objects.get(ind='5')
    return render(request, "books/history5.html", {"h5": h5})	

def articles(request):
    artc_list = Artc.objects.all()
       
    page = request.GET.get('page', 1)
    paginator = Paginator(artc_list, 7)
    try:
        artc_list = paginator.page(page)
    except PageNotAnInteger:
        artc_list = paginator.page(1)
    except EmptyPage:
        artc_list = paginator.page(paginator.num_pages)
    
    return render(request, "books/articles.html",{"artc_list": artc_list})	
def article1(request):
    a1 = Artc.objects.get(ind='1')
    return render(request, "books/article1.html", {"a1": a1})
def article2(request):
    a2 = Artc.objects.get(ind='2')
    return render(request, "books/article2.html", {"a2": a2})
def article3(request):
    a3 = Artc.objects.get(ind='3')
    return render(request, "books/article3.html", {"a3": a3})	
def dict(request):
    dict_list = Dict.objects.all().order_by('id')
    return render(request, "books/dict.html", {"dict_list": dict_list})	
def prose(request):
    pros_list = Pros.objects.all()
       
    page = request.GET.get('page', 1)
    paginator = Paginator(pros_list, 7)
    try:
        pros_list = paginator.page(page)
    except PageNotAnInteger:
        pros_list = paginator.page(1)
    except EmptyPage:
        pros_list = paginator.page(paginator.num_pages)
    
    return render(request, "books/prose.html",{"pros_list": pros_list})
def prose1(request):
    filepath=os.path.join('static', 'story1.pdf')
    return FileResponse(open(filepath,'rb'),content_type='application/pdf')	