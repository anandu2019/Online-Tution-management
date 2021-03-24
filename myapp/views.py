import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import userdetails,marksheet,Note_updated
from django.http import HttpResponse
from matplotlib.pyplot import figure
import mpld3

# Create your views here.
@login_required
def firstpage(request):
	return render(request,'Essen1.html')
'''
def register(request):
	return render(request,'register.html')
'''
def home(request):
	return render(request,'index.html')

def logoutview(request):
	logout(request)
	return redirect('/')

def loginview(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(request,username=username,password=password)
	if user is not None:
		login(request,user)
		return redirect('firstpage',{'user':username})
	else:
		return render(request,'index.html')

def sign_up(request):
	dict1={}
	form=UserCreationForm(request.POST)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(request,username=username,password=password)
			login(request,user)
			return redirect('login')
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{'form':form})

def adduser(request):
	dict1={}
	try:
		FName=request.POST["txt1"]
		LName=request.POST["txt2"]
		phone=request.POST["txt3"]
		Address=request.POST["txt5"]
		Adhar=request.POST["txt4"]
		regdetails=userdetails.objects.all()  
		if len(regdetails)==0:
			regdetails=userdetails(fname=FName,lname=LName,phone=phone,address=Address,adhar=Adhar)
			regdetails.save()
			print(regdetails)
			dict1["msg1"]="Added successfully"
			print(regdetails)

		for i in userdetails.objects.all():
			print('y')
			if i.phone==phone or i.adhar==Adhar:
				dict1["msg0"]="Already exists"
				return render(request,"Essen1.html",dict1)
			else:
				regdetails=userdetails(fname=FName,lname=LName,phone=phone,address=Address,adhar=Adhar)
				regdetails.save()
				print(regdetails)
				dict1["msg1"]="Added successfully"
				print(regdetails)
			return render(request,"Essen1.html",dict1)
	except Exception as e:
		print(e)
		dict1["msg2"]="Not Registered"
		return render(request,"Essen1.html",dict1)

def display(request):
	regdetails=userdetails.objects.all()
	return render(request,"Essen1.html",{'regdetails':regdetails})

def displaymarks(request):
	markdetails=marksheet.objects.all()
	return render(request,"results.html",{'markdetails':markdetails})
'''
def notes(request):
	notes=Notes.objects.all()
	return render(request,"attach.html",{'notes':notes})
'''
def fileview(request):
	context={'file':Note_updated.objects.all()}
	return render(request,"attach.html",context)

def download(request,path):
	file_path=os.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/field_name")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response

def aboutus(request):
	return render(request,"about.html")

'''
	dict1={}
	try:
		Maths=request.
		English=
		Gk=
		'''
def matplot(request):
	'''
	buf=BytesIO()
	plt.savefig(buf,format='png',dpi=300)
	image_base64=base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n','')
	buf.close()
	subject='Maths','English'
	'''
	abc=marksheet.objects.all()
	goals=[]
	for i in marksheet.objects.all():
		goals.append(i.Maths)
		goals.append(i.English)
	print(goals)
	colors=['y','r']
	plt.pie(goals,labels=subject,colors=colors,shadow=True,explode=(0.05,0.05),autopct= '%1.1f%%')
	plt.axis('equal')
	#plt.savefig('result.png')
	mpld3.show(plt)
	
	return render(request,"attach.html",{'plt':mpld3.show()})
