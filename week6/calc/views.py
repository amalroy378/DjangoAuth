from django.shortcuts import render,redirect
from .models import Actor,LatestUpdates
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')





@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    
    if request.method == 'POST':
       
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:

            auth.login(request,user)
           
            if request.user.is_superuser:
                     return redirect(adminchoice)
            return redirect(home)
        
        
        else:
            messages.info(request,"Invalid User")
            return redirect(login)
    else:
        return render(request,'login.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect(login)

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def cards(request): 
    dict_card={
        'card':Actor.objects.all()
    }
    return render(request,'cards.html',dict_card)


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login') 
def posts(request):
    dict_posts={
        'post':LatestUpdates.objects.all()
    }
    return render(request,'posts.html',dict_posts)




@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def signup(request,verify):
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        password =request.POST['password1']
        password2 =request.POST['password2']
        if password==password2:
            user=User.objects.create_user(email=email,username=name,password=password)
            user.save()
            print('verify before if ',verify)
            if verify==1:
                print('verify after if ',verify)
                return redirect(adminnew)
            return redirect(home)
        else:
            messages.info(request,'password  doesnt match')
            return redirect(signup)
    else:
        return render(request,'signup.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def adminchoice(request):
    if not request.user.is_superuser:
        return redirect(home)
    return render(request,'adminchoice.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def adminnew(request):
    if not request.user.is_superuser:
        return redirect(home)
    if request.method=='POST':
        search=request.POST['search']
        result=User.objects.filter(username__contains=search)
        return render(request,'search.html',{'result':result})

    dict_user={
        'user':User.objects.all()
    }
    
    return render(request,'adminnew.html',dict_user)
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deleterecord(request,userid):
    deleteuser=User.objects.filter(id=userid)
    deleteuser.delete()
    return redirect('adminnew')


def updaterecord(request,userid):
    username=request.POST['username']
    email=request.POST['email']
    update_user = User.objects.filter(id=userid)
    update_user.update(username=username,email=email)
    return redirect(adminnew)












    


