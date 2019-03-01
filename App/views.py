from django.shortcuts import render, redirect

# Create your views here.
from .forms import NewTeacherForm
from .models import Teacher

def index(request):
    allteachers=Teacher.object.all()
    return render(request, 'App/index.html', {'teacher_list': allteachers})

def teacher(request):
    new_form = NewUserForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')
    return render(request, 'App/users.html', {'userform': new_form})

def school(request, id):
    user = get_object_or_404(User, pk=id)
    read_form = NewUserForm(request.POST or None, instance=user)
    if read_form.is_valid():
        read_form.save()
        return redirect('index')
    return render(request, 'm_f_app/users.html', {'userform': read_form})

def subject(request, id):
    teacher = get_object_or_404(User, pk=id)
    read_form = NewTeacherForm(request.POST or None, instance=teacher)
        return redirect('index')
    return render(request, 'm_f_app/users.html', {'userform': read_form})

def hours(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    update_form = TeacherForm(request.POST or None, instance=teacher)
        return redirect('index')
    return render(request, 'App/teachers.html', {'teacherform': update_form})

def dateOfWork(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    delete_form = NewTeacherForm(request.POST or None, instance=teacher)
        return redirect('index')
    return render(request, 'App/teachers.html', {'teacherform': delete_form})

def dateOfEntry(request,id):
    teacher=get_object_or_404(Teacher, pk=id)
    delete_form=NewTeacherForm(request.POST or None, instance=teacher)
    return redirect('index')
    return render(request, 'App/teachers.html', {'teacherform': delete_form})
