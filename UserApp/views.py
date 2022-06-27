from django.shortcuts import redirect, render,HttpResponse

from UserApp.models import User_Info,personal_info,educational_details

# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):
    if(request.method == "GET"):
        return render(request,"signup.html",{})
    else:
        u1=User_Info()
        uname=request.POST['Username']
        pwd=request.POST['pswd']
        u1.username=uname
        u1.password=pwd
        u1.save()
        return redirect(home)
    
def login(request):
    if(request.method == "GET"):
        return render(request,"login.html",{})
    else:
        uname=request.POST["Username"]
        pwd=request.POST["pswd"]
        try:
            u1=User_Info.objects.get(username=uname,password=pwd)
            #create a session
            request.session["uname"]=uname
            return HttpResponse("successfully login")
        except:
            #pass
            return HttpResponse("login fail")
        
        return redirect(home)
            
    
def logout(request):
    request.session.clear()
    return redirect(home)

def personal_information(request):
    if(request.method == "GET"):
        return render(request,"personal_info.html",{})
    
    else:
        p1=personal_info()
        
        fullname=request.POST['fullname']
        phone_number=request.POST['phone_number']
        Gender=request.POST['Gender']
        dob=request.POST['dob']
        emailid=request.POST['emailid']
        Address=request.POST['Address']
        hobbies=request.POST['hobbies']
        languages_known=request.POST['languages_known']
        linkedin=request.POST['linkedin']
        github=request.POST['github']
        objective=request.POST['objective']
        
        p1.fullname=fullname
        p1.phone_number=phone_number
        p1.Gender=Gender
        p1.dob=dob
        p1.emailid=emailid
        p1.Address=Address
        p1.hobbies=hobbies
        p1.languages_known=languages_known
        p1.linkedin=linkedin
        p1.github=github
        p1.objective=objective
        
        p1.save()

        #return redirect(fields)
        print (p1.id)
    
        return render(request, 'fields.html',{"Pers":p1.id})
    print (p1.id)
    
   
   #testing purpose   
   
def educational_Details(request,Pers):
    if (request.method =="GET"):
        return render(request,"educational_details.html",{})  
    else:
        e1=educational_details()
        
        e1.nameOfExamination=request.POST['nameOfExamination']
        e1.institute=request.POST['institute']
        e1.university=request.POST['university']
        e1.percentage=request.POST['percentage']
        e1.yearOfcompletion=request.POST['yearOfcompletion']
        e1.perIn_id=personal_info.objects.get(id=Pers)
        
        e1.save()
        
        return render(request,"fields.html",{"Pers":Pers})
    
        
              
        
        
        