# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Hello WOrld!")

from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')