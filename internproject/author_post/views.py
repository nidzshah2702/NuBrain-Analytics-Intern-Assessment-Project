from django.shortcuts import render,redirect
from django.http import HttpResponse
from author_post.models import *
from django.core.paginator import Paginator


# Create your views here.

def author_details(request,id):
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




def post_details(request,id):
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
    post_list = Posts.objects.all()
    paginator = Paginator(post_list, 10) 

    page_number = request.GET.get('page')
    if(page_number==None):
        page_number=1
    page_obj = paginator.get_page(page_number)
    return render(request, 'viewposts.html', {'page_obj': page_obj})

