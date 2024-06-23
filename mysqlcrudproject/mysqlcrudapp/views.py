from django.shortcuts import render,redirect
from mysqlcrudapp.forms import StudentForm
from django.http import HttpResponse
from mysqlcrudapp.models import Student

# Create your views here.
def insert(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Data inserted into Database</h2>")
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})


def display(request):
    students = Student.objects.all()
    return render(request,'display.html',{'students':students})

def edit(request,id):
    student = Student.objects.get(id=id)
    return render(request,'edit.html',{'student':student})

def update(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
        return redirect('/display')
    return render(request,'edit.html',{'student':student})

def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/display')
