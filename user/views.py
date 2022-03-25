from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def SignUp(request, *args,**kwargs):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_c = request.POST["password_c"]
        #phone = request.POST["phone"]

        if password==password_c:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('SignUp')
            elif User.objects.filter(username=username):
                messages.info(request,'Username is already used.')
                return redirect('SignUp')
            else:
                user =User.objects.create_user(username =username,first_name=first_name,last_name = last_name,email=email,password=password)
                user.save();
                messages.info(request,'User created succesfully')
                return redirect('successfulSignUp')
        else:
            messages.info(request,'Password did not match')
            return redirect('SignUp')
    else:
        return render(request,'SignUp.html')




    return render(request,'SignUp.html',{})

def signIn(request,*args,**kwargs):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('signIn')
    else:
        return render(request,'signIn.html',{})

def signOut(request,*args, **kwargs):
    auth.logout(request)
    return redirect('/')

def successfulSignUp(request):
    return render(request,'successfulSignUp.html',)
