from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from app.fixtures.fixtures import *
from app.controller import categoryCRUD, urlCRUD, symbolCRUD


# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')


def fixtures(request):
    # add_category()
    # add_channels()
    # add_symbols()
    add_keywords()
    return HttpResponse(';')
