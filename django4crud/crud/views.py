from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def insertData(request):

    if request.method=='POST':
        
        name=request.POST.get('name')
        age=request.POST.get('age')
        major=request.POST.get('major')
        gender=request.POST.get('gender')
        print(name, age, major, gender)
        query=Student(name=name, age=age, major=major, gender=gender)
        query.save()
        messages.success(request, "Your data inserted! :D")
        return redirect("/")
    
    return render(request, 'index.html')

def updateData(request, id):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        major=request.POST['major']
        gender=request.POST['gender']
        
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.major=major
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.info(request, "Your data changed! ^-^")
        return redirect("/")
        # print(name, age, major, gender)
        
    

    info=Student.objects.get(id=id)
    context={"info":info}
    return render(request, 'edit.html', context)

def deleteData(request, id):
    info=Student.objects.get(id=id)
    info.delete()
    messages.error(request,"Data deleted :-(")
    return redirect("/")

    