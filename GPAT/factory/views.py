from django.shortcuts import render,redirect
from factory.forms import LoginForm
from GPAT import connect
import pyrebase
from django.contrib import auth
import time
from datetime import datetime,timezone
import matplotlib.pyplot as plt,mpld3
import pytz
import sys
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
#import factory.breezometer
plotly.tools.set_credentials_file(username='sunamyagupta', api_key='qN9YgaKDKqLNmuokTael')
#sns.set(style="ticks", color_codes=True)
# Create your views here.
def home(request):
   return render(request, "factory/templates/index.html", {})
def login(request):
	return render(request, "factory/templates/login.html", {})
def signup(request):
	return render(request,"factory/templates/index2.html",{})
def adminn(request):
	return render(request,"factory/templates/login1.html",{})
def profile(request):
	email=request.POST.get('email')
	passw=request.POST.get('password')
	try:
		user=connect.auth.sign_in_with_email_and_password(email,passw)
	except:
		message="Invalid Credentials"
		return render(request,"factory/templates/login.html",{"message":message})
	session_id=user['idToken']
	request.session['uid']=str(session_id)
	idtoken=request.session['uid']
	a=connect.auth.get_account_info(idtoken)
	a=a['users']
	a=a[0]
	a=a['localId']
	'''d=breezometer.breezometer1()
	if d==1:
		print("ERROR")
	else:
		connect.db.child("Users").child(a).child("Factory").child('1558769129').child("Air Polluatnts").set(data)'''
	name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
	data=list(connect.db.child("Users").child(a).child("Factory").child('1558769129').child('Air Polluatnts').get().val().items())
	dat1=list(connect.db.child("Users").child(a).child("Factory").child('1558769129').child('Sensors Data').get().val().items())
	sensor_n=[]
	sensor_v=[]
	for x in data:
		sensor_n.append(x[0])
		sensor_v.append(x[1])
	sensor_n1=[]
	sensor_v1=[]
	for x in dat1:
		sensor_n1.append(x[0])
		sensor_v1.append(x[1])
	trace1 = [go.Bar(
    x=sensor_n,
    y=sensor_v,
    name='Air Pollutants Index Value',
    marker=dict(
        color='rgb(55, 83, 109)'))]
	layout = go.Layout(
    title='Real Time Air Pollutants Index Value',
    xaxis=dict(
    	title='Pollutants',
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='Index Value',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ))
	fig = go.Figure(data=trace1, layout=layout)
	py.plot(trace1)
	trace2 = [go.Bar(
    x=sensor_n1,
    y=sensor_v1,
    name='Sensors Data',
    marker=dict(
        color='rgb(55, 83, 109)'))]
	py.plot(trace2)
	return render(request, "factory/templates/index1.html", {"username":name})
def dash(request):
	idtoken=request.session['uid']
	a=connect.auth.get_account_info(idtoken)
	a=a['users']
	a=a[0]
	a=a['localId']
	name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
	return render(request, "factory/templates/index1.html", {"username":name})
def logout(request):
	auth.logout(request)
	return render(request, "factory/templates/index.html", {})
def postsignup(request):
	f_name=request.POST.get('first_name')
	l_name=request.POST.get('last_name')
	position=request.POST.get('position')
	company=request.POST.get('dob')
	scale=request.POST.get('Scale')
	street=request.POST.get('street')
	zip1=request.POST.get('zip')
	city=request.POST.get('city')
	country=request.POST.get('country')
	phone=request.POST.get('phone')
	email=request.POST.get('your_email')
	password=request.POST.get('your_pass')
	print(email," ",password)
	try:
		user=connect.auth.create_user_with_email_and_password(email,password)
		uid=user['localId']
		message="Account created successfully!"
		data={"First Name":f_name,"Last Name":l_name,"Position":position,"Date of Birth":dob,"Street":street,"Zip":zip1,"City":city,"Country":country,"Phone":phone,"Email":email}
		connect.db.child("Users").child(uid).child("details").set(data)
		return render(request, "factory/templates/index.html", {"message":message})
	except:
		message="Error is : "+str(sys.exc_info()[0])+". Can`t create account"
		return render(request, "factory/templates/index2.html", {"message":message})
def approve(request):
	idtoken=request.session['uid']
	a=connect.auth.get_account_info(idtoken)
	a=a['users']
	a=a[0]
	a=a['localId']
	name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
	data=list(connect.db.child("Users").child(a).child("Factory").get().val().items())
	t=[]
	city=[]
	scale=[]
	nm=[]
	typ=[]
	print(data)
	try:
		for x in data:
			status=connect.db.child("Users").child(a).child("Factory").child(x[0]).child("Status").get().val()
			print(status)
			if status=="Approved":
				t.append(x[0])
		for y in t:
			d=list(connect.db.child("Users").child(a).child("Factory").child(y).get().val().items())
			city.append(d[1][1])
			scale.append(d[4][1])
			nm.append(d[5][1])
			typ.append(d[6][1])
		com=zip(city,scale,nm,typ)
		return render(request,"factory/templates/denied.html",{"username":name,"com":com})
	except:
		message="Error is : "+str(sys.exc_info()[0])+". No applications found"
		return render(request, "factory/templates/index1.html", {"message":message})
def denied(request):
	idtoken=request.session['uid']
	a=connect.auth.get_account_info(idtoken)
	a=a['users']
	a=a[0]
	a=a['localId']
	name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
	data=list(connect.db.child("Users").child(a).child("Factory").get().val().items())
	t=[]
	city=[]
	scale=[]
	nm=[]
	typ=[]
	print(data)
	try:
		for x in data:
			status=connect.db.child("Users").child(a).child("Factory").child(x[0]).child("Status").get().val()
			print(status)
			if status=="Denied":
				t.append(x[0])
		for y in t:
			d=list(connect.db.child("Users").child(a).child("Factory").child(y).get().val().items())
			city.append(d[1][1])
			scale.append(d[4][1])
			nm.append(d[5][1])
			typ.append(d[6][1])
		com=zip(city,scale,nm,typ)
		return render(request,"factory/templates/denied.html",{"username":name,"com":com})
	except:
		message="Error is : "+str(sys.exc_info()[0])+". No applications found"
		return render(request, "factory/templates/index1.html", {"message":message})
def pending(request):
	idtoken=request.session['uid']
	a=connect.auth.get_account_info(idtoken)
	a=a['users']
	a=a[0]
	a=a['localId']
	name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
	data=list(connect.db.child("Users").child(a).child("Factory").get().val().items())
	t=[]
	city=[]
	scale=[]
	nm=[]
	typ=[]
	print(data)
	try:
		for x in data:
			status=connect.db.child("Users").child(a).child("Factory").child(x[0]).child("Status").get().val()
			print(status)
			if status=="Pending":
				t.append(x[0])
		for y in t:
			d=list(connect.db.child("Users").child(a).child("Factory").child(y).get().val().items())
			city.append(d[1][1])
			scale.append(d[4][1])
			nm.append(d[5][1])
			typ.append(d[6][1])
		com=zip(city,scale,nm,typ)
		return render(request,"factory/templates/denied.html",{"username":name,"com":com})
	except:
		message="Error is : "+str(sys.exc_info()[0])+". No applications found"
		return render(request, "factory/templates/index1.html", {"message":message})
def form(request):
	idtoken=request.session['uid']
	a=connect.auth.get_account_info(idtoken)
	a=a['users']
	a=a[0]
	a=a['localId']
	name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
	return render(request,"factory/templates/forms.html",{"username":name})
def renew(request):
	idtoken=request.session['uid']
	a=connect.auth.get_account_info(idtoken)
	a=a['users']
	a=a[0]
	a=a['localId']
	name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
	return render(request,"factory/templates/renew.html",{"username":name})
def postadmin(request):
	email=request.POST.get('email')
	password=request.POST.get('password')
	print(email," ",password)
	if (email=="admin@gmail.com" and password=="admingpat"):
		return render(request, "factory/templates/admin.html",{})
	else:
		message="Invalid Admin Credentials"
		return render(request, "factory/templates/login1.html", {"message":message})
	return render(request, "factory/templates/admin.html",{})
def adminrequest(request):
	area=request.POST.get('area')
	return render(request, "factory/templates/application.html",{"area":area})
def factoryprofile(request):
	return render(request, "factory/templates/factoryprofile.html",{})
def formdata(request):
	factoryname=request.POST.get('factoryname')
	factorylocation=request.POST.get('factorylocation')
	factorycity=request.POST.get('factorycity')
	factorycountry=request.POST.get('factorycountry')
	factoryscale=request.POST.get('factoryscale')
	factorytype=request.POST.get('factorytype')
	tz=pytz.timezone('Asia/Kolkata')
	time_now=datetime.now(timezone.utc).astimezone(tz)
	millis=int(time.mktime(time_now.timetuple()))
	idtoken=request.session['uid']
	try:
		a=connect.auth.get_account_info(idtoken)
		a=a['users']
		a=a[0]
		a=a['localId']
		data={"Factory Name":factoryname,"Factory Location":factorylocation,"Factory City":factorycity,"Factory Country":factorycountry,"Factory Scale":factoryscale,"Factory Type":factorytype,"Request Registered":str(time_now),"Status":"Pending"}
		connect.db.child('Users').child(a).child("Factory").child(millis).set(data)
		name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
		return render(request, "factory/templates/forms.html",{"message":"Registration Request successfully registered!","username":name})
	except:
		message="Error is : "+str(sys.exc_info()[0])+". Failed to register Factory."
		a=connect.auth.get_account_info(idtoken)
		a=a['users']
		a=a[0]
		a=a['localId']
		name=connect.db.child("Users").child(a).child("details").child('First Name').get().val()
		return render(request, "factory/templates/forms.html", {"message":message,"username":name})