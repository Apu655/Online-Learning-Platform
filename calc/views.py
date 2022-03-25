from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.
def home_view(request,*args,**kwargs):
    courses =  Course.objects.all()

    return render(request,'test1.html',{'title':'home','courses':courses})
    

def navbar_view(request,*args,**kwargs):
    return render(request,'navbar.html',{'title':'navbar'})

def search_view(request,*args,**kwargs):
    if request.method =="GET":
        search = request.GET["searched"]
        if search =="":
            return render(request,'search.html',{'searched':'Nothing','courses':[]})
        else:
            courses = Course.objects.filter(name__contains=search)
            if courses:
                return render(request,'search.html',{'searched':search,'courses':courses})

            else:
                return render(request,'search.html',{'searched':search,'no_result':'No result found'})
    else:
        return render(request,'search.html',{})
def course_view(request,*args,**kwargs):
    return render(request,'course.html',{})