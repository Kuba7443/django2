from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')
def aboud(request):
    return render(request, 'main/aboud.html')