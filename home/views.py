from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mock(request):
    return HttpResponse('This is mock api')