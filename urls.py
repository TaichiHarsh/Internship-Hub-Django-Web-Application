from django.urls import path,include
from .import views,student_views
urlpatterns=[
    path("",views.home),
    path("about/",views.about_us,name="about_us"),
    path("contact/",views.contact_us,name="contact_us"),
    path("courses/",views.viewcourses,name="viewcourses"),
    path("login/",student_views.login,name="login"),
    path("student_home/",student_views.show_home,name="student_home")
]