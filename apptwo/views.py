from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    mydict={'insert_me':'I am coming from help/helppage.html'}
    return render(request,'help/helppage.html',context=mydict)