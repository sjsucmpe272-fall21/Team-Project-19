from django.db import models

from django.contrib.auth.models import User


def user_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = instance.firstname + instance.lastname
    filename = name +'.'+ ext 
    return 'Faculty_Images/{}'.format(filename)

class Faculty(models.Model):

    user = models.OneToOneField(User, null = True, blank = True, on_delete= models.CASCADE)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to=user_directory_path ,null=True, blank=True)

    def __str__(self):
        return str(self.firstname + " " + self.lastname)


def student_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = instance.registration_id # + "_" + instance.branch  + "_" + instance.section
    filename = name +'.'+ ext 
    return 'Student_Images/{}/{}/{}'.format(instance.branch,instance.section,filename)

class Student(models.Model):

    #Branches will include SJSU Computer Engineering Graduate Program Courses (SE, CMPE, AI)
    BRANCH = (
        ('CMPE 200','CMPE 200'),
        ('CMPE 202','CMPE 202'),
        ('CMPE 203','CMPE 203'),
        ('CMPE 206','CMPE 206'),
        ('CMPE 207','CMPE 207'),
        ('CMPE 208','CMPE 208'),
        ('CMPE 209','CMPE 209'),
        ('CMPE 212','CMPE 212'),
        ('CMPE 213','CMPE 213'),
        ('CMPE 214','CMPE 214'),
        ('CMPE 217','CMPE 217'),
        ('CMPE 219','CMPE 219'),
        ('CMPE 220','CMPE 220'),
        ('CMPE 221','CMPE 221'),
        ('CMPE 225','CMPE 225'),
        ('CMPE 226','CMPE 226'),
        ('CMPE 227','CMPE 227'),
        ('CMPE 232','CMPE 232'),
        ('CMPE 234','CMPE 234'),
        ('CMPE 235','CMPE 235'),
        ('CMPE 236','CMPE 236'),
        ('CMPE 237','CMPE 237'),
        ('CMPE 238','CMPE 238'),
        ('CMPE 239','CMPE 239'),
        ('CMPE 240','CMPE 240'),
        ('CMPE 241','CMPE 241'),
        ('CMPE 242','CMPE 242'),
        ('CMPE 243','CMPE 243'),
        ('CMPE 244','CMPE 244'),
        ('CMPE 245','CMPE 245'),
        ('CMPE 249','CMPE 249'),
        ('CMPE 250','CMPE 250'),
        ('CMPE 251','CMPE 251'),
        ('CMPE 252','CMPE 252'),
        ('CMPE 255','CMPE 255'),
        ('CMPE 256','CMPE 256'),
        ('CMPE 257','CMPE 257'),
        ('CMPE 258','CMPE 258'),
        ('CMPE 260','CMPE 260'),
        ('CMPE 261','CMPE 261'),
        ('CMPE 262','CMPE 262'),
        ('CMPE 264','CMPE 264'),
        ('CMPE 265','CMPE 265'),
        ('CMPE 266','CMPE 266'),
        ('CMPE 270','CMPE 270'),
        ('CMPE 271','CMPE 271'),
        ('CMPE 272','CMPE 272'),
        ('CMPE 273','CMPE 273'),
        ('CMPE 274','CMPE 274'),
        ('CMPE 275','CMPE 275'),
        ('CMPE 276','CMPE 276'),
        ('CMPE 277','CMPE 277'),
        ('CMPE 278','CMPE 278'),
        ('CMPE 279','CMPE 279'),
        ('CMPE 281','CMPE 281'),
        ('CMPE 282','CMPE 282'),
        ('CMPE 283','CMPE 283'),
        ('CMPE 284','CMPE 284'),
        ('CMPE 285','CMPE 285'),
        ('CMPE 286','CMPE 286'),
        ('CMPE 287','CMPE 287'),
        ('CMPE 290','CMPE 290'),
        ('CMPE 294','CMPE 294'),
        ('CMPE 295A','CMPE 295A'),
        ('CMPE 295B','CMPE 295B'),
        ('CMPE 297','CMPE 297'),
        ('CMPE 298','CMPE 298'),
        ('CMPE 299A','CMPE 299A'),
        ('CMPE 299B','CMPE 299B'),
        ('ENGR 200W','ENGR 200W'),
        ('ISE 201','ISE 201'),
        ('ISE 244','ISE 244'),
    )
    SECTION = (
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
    )

    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    registration_id = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=100, null=True, choices=BRANCH)
    section = models.CharField(max_length=100, null=True, choices=SECTION)
    profile_pic = models.ImageField(upload_to=student_directory_path ,null=True, blank=True)


    def __str__(self):
        return str(self.registration_id)

class Attendence(models.Model):
    Faculty_Name = models.CharField(max_length=200, null=True, blank=True)
    Student_ID = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add = True, null = True)
    time = models.TimeField(auto_now_add=True, null = True)
    branch = models.CharField(max_length=200, null = True)
    section = models.CharField(max_length=200, null = True)
    period = models.CharField(max_length=200, null = True)
    status = models.CharField(max_length=200, null = True, default='Absent')

    def __str__(self):
        return str(self.Student_ID + "_" + str(self.date)+ "_" + str(self.period))