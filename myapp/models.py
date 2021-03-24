from django.db import models
from django.db.models import Model
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.
class RegisterForm(models.Model):
	name=models.CharField(max_length=20)
	ph_number=models.IntegerField()
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=20)
class UserRegistration(models.Model):
	Firstname=models.CharField(max_length=20)
	Lastname=models.CharField(max_length=20)
	phone = PhoneNumberField(blank=True)
	Adharnumber=models.CharField(max_length=20)
	address=models.TextField()
	city=models.CharField(max_length=20)
	pin_code=models.CharField(max_length=4)

class userdetails(models.Model):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	phone=models.CharField(max_length=10)
	address=models.CharField(max_length=40)
	adhar=models.CharField(max_length=15)
class marksheet(models.Model):
	Maths=models.CharField(max_length=10)
	English=models.CharField(max_length=10)
	GK=models.CharField(max_length=10)
class Notes(models.Model):
	pass
	#field_name = models.ImageField(upload_to='post-img', height_field=None, width_field=None, max_length=100)
class Note_updated(models.Model):
	field_name = models.FileField(upload_to='post-img')
	title = models.CharField(max_length=50)
	
    

	
	

