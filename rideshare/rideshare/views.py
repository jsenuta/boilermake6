import pyrebase
from django.shortcuts import render
 
config = {
    'apiKey': "AIzaSyDI2z3pBo_2Fk4itX3CIg72XX8sMqsqalc",
    'authDomain': "boilermake6-a5da9.firebaseapp.com",
    'databaseURL': "https://boilermake6-a5da9.firebaseio.com",
    'projectId': "boilermake6-a5da9",
    'storageBucket': "boilermake6-a5da9.appspot.com",
    'messagingSenderId': "188678498556"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
def singIn(request):
	return render(request, "signIn.html")
def postsign(request):
	email=request.POST.get('email')
	passw = request.POST.get("pass")
	try:
		user = auth.sign_in_with_email_and_password(email,passw)
	except:
		message = "invalid cerediantials"

	return render(request,"signIn.html",{"msg":message})
	print(user)
	return render(request, "welcome.html",{"e":email})
def home(request):
	return render(request, "home.html", {"request":request})