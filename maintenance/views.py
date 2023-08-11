from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is the homepage')


def maintenance(request):
    return render(request, 'maintenance/maintenance.html')