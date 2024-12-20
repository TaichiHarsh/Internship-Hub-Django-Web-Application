from django.shortcuts import render,HttpResponse
from .models import Notice,Course
# Create your views here.
def home(request):

    #return HttpResponse("hello browser")
    notice_object_list=Notice.objects.all() # it is equivalent to (select*from notice)
    # print(type(notice_object_list))
    # for n in notice_object_list:
    #     print(f"notice content is {n.notice_contents}")

        # print(type(n))
    notice_contents={
        "notice_key":notice_object_list,
        "title":"MyHomePage"
    }
    return render(request,"myapp/html/index.html",notice_contents)
def about_us(request):
    #return HttpResponse("this is about us")
    return render(request,"myapp/html/about_us.html")
def contact_us(request):
    #return HttpResponse("<h1>this is contact us</h1>")
    return render(request,"myapp/html/contact_us.html")

def viewcourses(request):
    course_object_list=Course.objects.all()
    course_dict={
        "course_key":course_object_list
    }
    #return HttpResponse("<h1>this is contact us</h1>")
    return render(request,"myapp/html/viewcourses.html",course_dict)

        
    