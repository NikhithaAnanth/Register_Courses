from django.shortcuts import render

# Create your views here.
from .forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'newforms/index.html',{'form':form1,'param1':"THANK YOU FOR RIGISTERING !!"})
    else:
        form1=inputform()
    return render(request,'newforms/index.html',{'form':form1})