from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher

def teacher_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TeacherForm()
        else:
            teacher = Teacher.objects.get(pk=id)
            form = TeacherForm(instance=teacher)
        return render(request, "teachapp/teacher_form.html", {'form': form})
    else:
        if id == 0:
            form = TeacherForm(request.POST)
        else:
            teacher = Teacher.objects.get(pk=id)
            form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
        return redirect('/teachers')

def teachers_list(request):
    obj = {'teachers_list': Teacher.objects.all()}
    return render(request, "teachapp/teachers.html", obj)

def teachers_delete(request, id):
    teacher = Teacher.objects.get(pk=id)
    teacher.delete()
    return redirect('/teachers')
