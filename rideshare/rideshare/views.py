#import pyrebase
from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post

config = {
    'apiKey': "AIzaSyDI2z3pBo_2Fk4itX3CIg72XX8sMqsqalc",
    'authDomain': "boilermake6-a5da9.firebaseapp.com",
    'databaseURL': "https://boilermake6-a5da9.firebaseio.com",
    'projectId': "boilermake6-a5da9",
    'storageBucket': "boilermake6-a5da9.appspot.com",
    'messagingSenderId': "188678498556"
}
#firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
def signIn(request):
	return render(request, "signIn.html")
def postsign(request):
	email=request.POST.get('email')
	passw = request.POST.get("pass")
	#try:
	#	user = auth.sign_in_with_email_and_password(email,passw)
	#except:
	#	message = "invalid cerediantials"

	return render(request,"signIn.html",{"msg":message})
	print(user)
	return render(request, "welcome.html",{"e":email})
def home(request):
	return render(request, "home.html", {"request":request})
def ridepost(request):
    return render(request, "ridepost.html", {"request":request})
def viewRides(request):
    return render(request, "viewRides.html", {"request":request})
def post_list(request):
	#posts = Post.objects.order('published_date')
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'post_list.html', {'posts': posts})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.publish()
            return redirect('/listings/')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

