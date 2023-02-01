from django.db import models

# Create your models here.
class SelfDrive(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length = 100)
    email = models.EmailField(default="mc@gmail.com",max_length= 100)
    phoneNo = models.IntegerField()
    id_No= models.IntegerField()
    CAR_TYPE = (
        ('S','Subaru'),
        ('P','Premio'),
        ('L','Landcruiser Prado'),
        ('V','V8'),
        ('VT','Vitz'),
        ('M','Mazda'),
        ('B','Mercedes Benz')
    )
    type_Of_Car = models.CharField(max_length=30,choices = CAR_TYPE,default='1')

    def __str__(self):
        return self.email
    
class PostCar(models.Model):
    name = models.CharField(default = 'subaru',max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=1000000)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LetCar(models.Model):
    fname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(default="mc@gmail.com",max_length=100)
    phoneNo = models.IntegerField()
    id_No = models.IntegerField()
    located_At = models.CharField(max_length=100)
    let_Date = models.DateTimeField()
    duration_To_Let = models.CharField(max_length=100)
    CAR_TYPE = (
        ('S','Subaru'),
        ('P','Premio'),
        ('L','Landcruiser Prado'),
        ('V','V8'),
        ('VT','Vitz'),
        ('M','Mazda'),
        ('B','Mercedes Benz')
    )
    type_Of_Car_To_Let = models.CharField(max_length=30,choices = CAR_TYPE,default='1')

    def __str__ (self):
        return self.email
    
class TaxCab(models.Model):
    first_name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    no_of_passegers = models.IntegerField()
    your_Location = models.CharField(max_length=100)
    departure_Time = models.DateTimeField()
    distance_to_travel = models.CharField(max_length=100)

    def __str__(self):
        return self.your_Location
