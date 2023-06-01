from django.db import models

# Create your models here.

class Contact(models.Model):
    name =models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) :
        return self.email
    
class Enrollment(models.Model):
    fullName =models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    gender = models.CharField(max_length=20,)
    DOB = models.DateField(max_length=50)
    selectMemberShipPlans = models.CharField(max_length=200)
    selectTrainer = models.CharField(max_length=255)
    refrence = models.CharField(max_length=55)
    address = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    paymentStatus = models.CharField(max_length=55,blank=True)
    price = models.IntegerField(blank=True,null=True)
    dueDate = models.DateTimeField(blank=True,null=True)

    def __str__(self) :
        return self.fullName
    

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    gender = models.CharField(max_length=55)
    salary = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name


class MemberShipPlan(models.Model):
    plan = models.CharField(max_length=55)
    price = models.IntegerField()

    def __str__(self) :
        return self.plan
    

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='gallery')
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title


class Attendance(models.Model):
    phoneNumber = models.CharField(max_length=15)
    selectDate = models.DateTimeField(auto_now_add=True)
    login = models.CharField(max_length=255)
    logout = models.CharField(max_length=255)
    selectWorkout = models.CharField(max_length=255)
    trainedBy = models.CharField(max_length=255)

    # def __str__(self) :
    #     return self.phoneNumber