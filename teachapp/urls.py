from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_form, name = "register_teacher"),
    path('<int:id>/', views.teacher_form, name = "update_teacher"),
    path('delete/<int:id>/', views.teachers_delete, name = "delete_teacher"),
    path('teachers', views.teachers_list, name = "teachers_list")
]
