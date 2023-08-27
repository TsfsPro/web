from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения Rifle")

def category(request, catid):
    return HttpResponse(f"<h1>Страница категории приложения Rifle<h1/><p> {catid} </p>")

def arhive(request, year):
    return HttpResponse(f"<h3>Архив по годам -<p> {year}</p></h3>")