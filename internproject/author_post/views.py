from django.shortcuts import render,redirect
from django.http import HttpResponse
from author_post.models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.hashers import *
from django.contrib.auth.decorators import login_required




# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        birthdate=request.POST['birthdate']
        if not(User.objects.filter(email=email).exists()) :
            hashedpassword=make_password(password, salt=None, hasher='default')
            user=User(email=email,password=hashedpassword,is_staff=0,is_superuser=0)
            user.save()
            request.session['logged_in'] = True

            profile=UserProfileInfo(user=user,first_name=firstname,last_name=lastname,birthdate=birthdate)
            profile.save()

            return HttpResponseRedirect('/posts')
        else:
            error="*Email already exists"
            return render(request,'register.html',{'firstname':firstname,'error':error, 'email':email,'lastname':lastname})
    else:
        return render(request, 'register.html')

@csrf_exempt
def login(request):
    if request.method== 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = User.objects.get(email=email)
        if user is not None  and check_password(password,user.password):
             auth.login(request, user)
             request.session['logged_in'] = True

             return HttpResponseRedirect('/posts')
        else:
             error="Invalid Login"
             return render(request,'login.html',{'error':error})

    else:
        c = {}
        c.update(csrf(request))
        return render(request,'login.html', c)
   
    
@csrf_exempt
def author_details(request,id):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/auth/login')
    try:

        author=Authors.objects.get(id=id)
        count=Posts.objects.filter(author_id=id).count()
        context={}
        context['author']=author
        context['posts']=count
        print(author.birthdate)
        return render(request, 'authordetails.html',context)
    except:
        return render(request,'notfound.html')



@csrf_exempt
def post_details(request,id):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/auth/login')
    try: 
         post=Posts.objects.get(id=id)
         authid=post.author_id
         author=Authors.objects.get(id=authid)
         context={}
         context['author']=author
         context['post']=post
         return render(request, 'postdetails.html',context)
    except:
        return render(request,'notfound.html')

def view_posts(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/auth/login')
    post_list = Posts.objects.all()
    paginator = Paginator(post_list, 10) 

    page_number = request.GET.get('page')
    if page_number==None:
        page_number=1
    page_obj = paginator.get_page(page_number)
    return render(request, 'viewposts.html', {'page_obj': page_obj})


def logout(request):
    del request.session['logged_in']
    return HttpResponseRedirect('/auth/login')