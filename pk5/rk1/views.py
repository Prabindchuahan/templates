from django.shortcuts import render

# Create your views here.
def home(request):
    name = 'Prabind'
    cname = 'Java'
    price = 52
    course_details = {'nm':name,'cn':cname, 'pr':price}

    
    return render(request,'coursename/home.html',course_details)


def define(request):
    emp_name = 'hari'
    branch = "admin It Cse"
    salary = 2000
    emp = {'em': emp_name, 'br':branch ,'sl':salary}
    return render(request,'Employee/define.html',emp)


def course(request):
    return render(request,'Employee/define.html',{'nm':'prabind'})

def course1(request):
    student = { 'name':['Hari','Rama','Syama','Ravi']}
    print(student)
    return render(request,'Employee/define.html',student)

def student_details(request):
    stu = {'stu1': {'name':'Prabind','Education':'B.tech','Roll':103},
            'stu2': {'name':'Hari','Education':'B.tech','Roll':104},
            'stu3': {'name':'Radhesyam','Education':'B.tech','Roll':105},
            'stu4': {'name':'Ramu','Education':'B.tech','Roll':106}
            }
    student = {'student':stu}
    return render(request,'Employee/define.html',student)
    