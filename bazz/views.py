from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from service.models import Service




def homepage(request):
    #servicesdata =Service.objects.all()
    #print(servicesdata)
    #for a in servicesdata:
    #    print(a.service_tiltle)
    #data = {
        
    #    'servicedata':servicesdata
   # }
    return render(request,"homepage.html",)

def header(request):
    return render(request,"header.html")

def footer(request):
    return render(request,"footer.html")
def thanku(request):
    if request.method == "GET":
        output = request.GET.get('output')
    
    return render(request,"thank.html",{'output':output})



def viewpage(request,viewpage):
    return render(request,"footer.html")

def about(request,about):
    data={
        'title': "aboutus",
        'clist' : ['php','python','django'],
        'number': [1,2,3,4,5,6]
        
        
        
        
         }
    
    
    return render(request,"about.html",data)

def services(request):
    return render(request,"services.html")

def contact(request):
    data = {}
    finalans= 0
    try:         
        if request.method == "POST":   
           n1 = int(request.POST.get('name1'))
           n2 = int(request.POST.get('name2'))
           
           finalans = n1+n2
           data = {
               "n1":n1,
               "n2":n2,
               "output":finalans
           }
           
           url = "/thanku/?output={}".format(finalans)
           return HttpResponseRedirect(url)
     
    except:
        pass
    return render(request,"contact.html",data)


