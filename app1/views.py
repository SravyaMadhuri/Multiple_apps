from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_str(request):
    return HttpResponse('<h1> This is the string format response</h1>')
def HTMLPAGE(request):
    return render(request,'HTMLPAGE.html')