from django.shortcuts import render
from .models import Student
from django.contrib import messages
def show_home(request):
    return render(request,"myapp/student/student_home.html")
def login(request):
    if request.method == "GET":
    
        return render(request,"myapp/html/login.html")
    if request.method == "POST":
        
        s_id=request.POST["userid"]
        s_pass=request.POST.get("userpass")#another way to fetch data from dict
        print(s_id,s_pass)
        student_list=Student.objects.filter(student_id=s_id,student_password=s_pass)
        #select * from student where student_id=s_id and student_password=s_pass
        length=len(student_list)
        if length>0:
            return render(request,'myapp/student/student_home.html')
        else:
            messages.error(request,"Invalid Credentials")
            return render(request,'myapp/html/login.html')

    