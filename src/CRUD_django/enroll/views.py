from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.





###
####This function is to add and show data
###
def add_show_view(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)

        # if fm.is_valid():
        #     fm.save()
        #or we can do

        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=ps)
            reg.save()
            fm=StudentRegistration()

        
    else:
        fm=StudentRegistration()

    stud=User.objects.all()
    
    context={
        'form':fm,
        'stu':stud,
    }

    return render(request,'enroll/addandshow.html',context)



###
#### This function is to delete_data
###


def delete_record(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    


###
##### Function to update data
###
    
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        li=User.objects.get(pk=id)
        fm=StudentRegistration(instance=li)
        
    context={
        'form':fm,
    }
    return render(request,'enroll/updatestudent.html',context)