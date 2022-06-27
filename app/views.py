from django.http import HttpRequest, HttpResponse
from app.fixtures.fixtures import *


# Create your views here.
def home(request):
    add_category()
    add_channels()
    add_symbols()
    add_keywords()
    add_messages()
    return HttpResponse('Hello, World!')
