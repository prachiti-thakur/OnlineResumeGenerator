from turtle import bye
from django.shortcuts import redirect, render,HttpResponse

from UserApp.models import User_Info,personal_info,educational_details,certification,technical_skills,academic_project

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
        request.session.clear()
        return render(request,"login.html",{})
    else:
        uname=request.POST["Username"]
        pwd=request.POST["pswd"]
        try:
            u1=User_Info.objects.get(username=uname,password=pwd)
            #create a session
            request.session["uname"]=uname
            #return HttpResponse("successfully login")
        except:
            pass
            #return HttpResponse("login fail")
        
        return redirect(home)
            
    
def logout(request):
    request.session.clear()
    return redirect(home)

def personal_information(request):
    if(request.method == "GET"):
        if("uname" in request.session):
            return render(request,"personal_info.html",{})
        else:
            return redirect(login)
    
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
        return render(request, 'fields.html',{"Pers":p1.id})
    
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
    
        
def Certification(request,Pers):
    if (request.method =="GET"):
        return render(request,"certification.html",{})  
    else:
        
        c1=certification()
        
        c1.certification=request.POST['certification']
        c1.perIn_id=personal_info.objects.get(id=Pers)
        
        c1.save()
         
        return render(request,"fields.html",{"Pers":Pers})     
        
        
def Technical_Skills(request,Pers):
    if (request.method =="GET"):
        return render(request,"Technical_Skills.html",{})
    else:
        
        t1=technical_skills()
        
        t1.skills=request.POST['skills']
        t1.perIn_id=personal_info.objects.get(id=Pers)
        
        t1.save()
        
        return render(request,"fields.html",{"Pers":Pers})
        
               
def Academic_Project(request,Pers):
    if (request.method =="GET"):
        return render(request,"Academic_Project.html",{})
    else:
        a1=academic_project()
        
        a1.project_name=request.POST['project_name']
        a1.technologies_used=request.POST['technologies_used']
        a1.description=request.POST['description']
        a1.perIn_id=personal_info.objects.get(id=Pers)
        
        a1.save()
        
        return render(request,"fields.html",{"Pers":Pers})
    
def resume(request,Pers):
    
    Pers=personal_info.objects.get(id=Pers)
    Ed_d=educational_details.objects.filter(perIn_id=Pers)
    certi=certification.objects.filter(perIn_id=Pers)
    Tec_Skill=technical_skills.objects.filter(perIn_id=Pers)
    acd_p=academic_project.objects.filter(perIn_id=Pers)
    
    
    return render(request,"resume.html",{"Ed_d":Ed_d,"certi":certi,"Tec_Skill":Tec_Skill,"acd_p":acd_p,"Pers":Pers})
