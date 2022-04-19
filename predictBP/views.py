from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request, HttpRequest, response
from django.template import loader

def index(request):
    return render(request, 'predictBP/index.html')