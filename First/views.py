import sys

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from First.models import Employee
from First.forms  import EmpForm
# Create your views here.

def Display(request):
    emp=Employee.objects.all()
    return render(request,"show.html",{'e':emp})

def del_emp(request,id):
    e=Employee.objects.get(eid=id)
    e.delete()
    return redirect("/show")

def insert_emp(request):
    if request.method=="POST":
        form=EmpForm(request.POST)
        print("------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                print("----", sys.exc_info())
        else:
            pass
    else:
        form = EmpForm()

    return render(request,"insert_emp.html",{"form":form})

def edit_emp(request,id):
    emp=Employee.objects.get(eid=id)
    return render(request,"edit_emp.html",{"e":emp})

def update_emp(request,id):
    emp=Employee.objects.get(eid=id)
    form=EmpForm(request.POST,instance=emp)
    print("----",form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/show")
        except:
            pass
    else:
        print("-----",sys.exc_info())

    return render(request,"edit_emp.html",{"e":emp})