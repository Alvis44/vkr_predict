from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request, HttpRequest, response
from django.template import loader

import predictBP.pretictPy as pred

def index(request):
    return render(request, 'predictBP/index.html')

def matrix(request):
    if request.method == 'POST':
        context={'plotnost': request.POST['plotnost'],
                 'modulUprugosti': request.POST['modulUprugosti'],
                 'poverhPlotn': request.POST['poverhPlotn'],
                 'modulUprugostiRast': request.POST['modulUprugostiRast'],
                 'prochnRast': request.POST['prochnRast'],
                 'shagNash': request.POST['shagNash'],
                 'plotNash': request.POST['plotNash'],
                 'result': pred.predict(request.POST, 'matrix')}
    else:
        context={'result': ''}
    return render(request, 'predictBP/matrix.html', context=context)

def modul(request):
    if request.method == 'POST':
        result = pred.predict(request.POST, 'modul')
        if type(result) == str:
            result1 = result
            result2 = result
        else:
            result1 = result[0]
            result2 = result[1]

        context={'plotnost': request.POST['plotnost'],
                 'modulUprugosti': request.POST['modulUprugosti'],
                 'poverhPlotn': request.POST['poverhPlotn'],
                 'matr': request.POST['matr'],
                 'shagNash': request.POST['shagNash'],
                 'plotNash': request.POST['plotNash'],
                 'resultmodulUprugostiRast': result1,
                 'resultprochnRast': result2}
    else:
        context={'resultmodulUprugostiRast': '', 'resultprochnRast': ''}
    return render(request, 'predictBP/modul.html', context=context)