from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_str(request):
    return HttpResponse('<h1> This is the app2 string format response</h1>')
def PAGES(request):
    return render(request,'LMTHPAGE.html')