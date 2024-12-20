from django.db import models
from django.utils import timezone
class Notice(models.Model):
    notice_contents=models.CharField(max_length=45)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.notice_contents
        
## course model##
class Course(models.Model):
    course_name=models.CharField(max_length=45,primary_key=True)
    course_fees=models.IntegerField()
    course_duration=models.CharField(max_length=40)
    course_contents=models.TextField(blank=True)
    course_pic=models.FileField(max_length=200,upload_to="myapp/course_pic",default="")

    def __str__(self):
        return self.course_name

#student model##
gender=[
    ("m","male"),
    ("f","female")
]

#cascade
# donothings
class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=45) 
    email=models.EmailField(max_length=45) 
    phone=models.CharField(max_length=10) 
    student_id=models.CharField(max_length=40,primary_key=True,default="") 
    student_password=models.CharField(max_length=40)
    gender=models.CharField(max_length=6,choices=gender) 
    description=models.TextField() 
    address=models.TextField()  
    student_pic=models.FileField(max_length=200,upload_to="myapp/student_pic",default="")      

    def __str__(self):
        return self.name