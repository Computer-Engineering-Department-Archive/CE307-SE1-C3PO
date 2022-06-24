from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from app.fixtures.fixtures import *
from app.model import categoryCRUD, urlCRUD, symbolCRUD
from app.controller import botnet, analysis


# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')


def fixtures(request):
    add_category()
    add_channels()
    add_symbols()
    add_keywords()
    return HttpResponse('DONE!')


def urls(request):
    return HttpResponse(urlCRUD.read_all(), content_type="application/json")


def read_all(request):
    return HttpResponse(botnet.read_all_messages())
