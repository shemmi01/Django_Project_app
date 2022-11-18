from cmath import phase
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from.models import Role, Employee, Department
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')



def all_emp(request):
    emps = Employee.objects.all()
    context= {
        'emps' :emps

    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == "POST" :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary =int( request.POST['salary'])
        Bonus= int(request.POST['Bonus'])
        Phone = int(request.POST[' Phone'])
        Department =int( request.POST['Department'])
        Role = int(request.POST[' Role'])
        new_emp = Employee(first_name = "first_name", last_name='last_name',salary='salary',Bonus='Bonus',Phone='Phone',dept_id= 'Department', role_id='role' , hire_date='datetime.now' )
        new_emp.save()
        return HttpResponse("Employee added Successfully")
    elif request.method=='GET':
    
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An exception occured: Employee has not been added")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse('Please enter emp id value')

    emps = Employee.objects.all()
    context= {
        'emps' :emps
    }

    return render(request,'remove_emp.html')
 
def filter_emp(request):
    return render(request,'filter_emp.html')
 
 

