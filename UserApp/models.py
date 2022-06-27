from django.db import models

# Create your models here.
class User_Info(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    
    class Meta:
        db_table = "userInfo"
        
class personal_info(models.Model):
    fullname= models.CharField(max_length=20)
    phone_number=models.IntegerField
    Gender=models.CharField(max_length=6)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    emailid=models.EmailField(max_length=50)
    Address=models.TextField(max_length=225)
    hobbies=models.CharField(max_length=100)
    languages_known=models.CharField(max_length=50)
    linkedin=models.CharField(max_length=200)
    github=models.CharField(max_length=200)
    objective=models.TextField(max_length=1000)
    
    class Meta:
        db_table="personal_info"
    

class educational_details(models.Model):
    nameOfExamination = models.CharField(max_length=50)
    institute=models.CharField(max_length=500)
    university=models.CharField(max_length=100)
    percentage=models.CharField(max_length=10)
    yearOfcompletion=models.IntegerField
    perIn_id = models.ForeignKey(personal_info,on_delete=models.CASCADE)

    class Meta:
        db_table="educational_details"
    
class certification(models.Model):
    certification=models.CharField(max_length=100)
    perIn_id = models.ForeignKey(personal_info,on_delete=models.CASCADE)

    class Meta:
        db_table="certification"
        
   
class technical_skills(models.Model):
    skills= models.CharField(max_length=100)
    perIn_id = models.ForeignKey(personal_info,on_delete=models.CASCADE)
    
    class Meta:
        db_table="technical_skills"
        
class academic_project(models.Model):
    project_name= models.CharField(max_length=100)
    technologies_used=models.CharField(max_length=200)
    description=models.TextField(max_length=1000)
    perIn_id = models.ForeignKey(personal_info,on_delete=models.CASCADE)
    
    class Meta:
        db_table="academic_project"
    

    
    
    