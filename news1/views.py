from django.shortcuts import render,redirect
from news1.models import *
from news1.forms import *
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.


def showhomenews(request):
    breaking = news.objects.filter(tag='Breaking',status='active').order_by('-id')[:3]
    latest = news.objects.filter(tag='latest',status='active').order_by('-id')[:4]
    tech=news.objects.filter(category_id=2,status='active').order_by('-id')[:3]
    fashion= news.objects.filter( category_id=1,status='active').order_by('-id')[:4]
    sport= news.objects.filter(category_id=9,status='active').order_by('-id')[:5]
    travel=news.objects.filter(category_id=4,status='active').order_by('-id')[:2]
    context = {
        'breaking': breaking,
        'tech': tech,
        'fashion': fashion,
        'sport': sport,
        'latest':latest,
	'travel':travel
        
    }
    return render(request, "newsportal.html", context)
	
class socialpageview(TemplateView):
	template_name="social.html"	

class aboutview(TemplateView):
	template_name="about.html"	


class testpageview(TemplateView):
	template_name="test.html"	
	
class test2pageview(TemplateView):
	template_name="test2.html"	

class contactpageview(TemplateView):
	template_name="contact.html"

def shownews(request, cat):
    newsobject = news.objects.filter(category_id=cat,status='active')
    catobject=category.objects.get(id=cat)
    context = {
        'newsobject': newsobject,
        'catobject':catobject,
    }
    return render(request, "newsdetail.html", context)	

def detailnewsview(request, id):
    newsobject = news.objects.get(id=id)
    com=comment.objects.select_related('userid').filter(newsid_id=id)
    context = {
        'newsobject': newsobject,
        'com':com
        
    }
    return render(request, "detailnews.html", context)	

def videonewsview(request,id):
	video=videonews.objects.select_related('categoryid').filter(categoryid_id=id)
	catobj=category.objects.get(id=id)
	return render(request,"videonews.html",{'video':video,'catobj':catobj})
	
	
	
def insert(request):
	if request.method=='POST':
		form=contactform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/newsportal/')
			except:
				pass
	
	else:
		form=contactform()
		
	return render(request,'contact.html',{'form':form})	

def signup(request):
    if request.method=='POST':
        form=signform(request.POST)
        if form.is_valid():
            try:
                user=form.save()
                login(request,user)
                return redirect('/newsportal/')
            except:
                pass
    else:
        form=signform()
    return render(request,'registration/sign.html',{'form':form})

def insertcomment(request):
    if request.method=='POST':
        form=commentform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/newsportal/')
            except:
                pass
    else:
        form=commentform()
    return render(request,'detailnews.html',{'form':form})    
    
def commentview(request,id):
    comm=comment.objects.filter(userid_id=id).select_related('newsid')
    context={
        'comm':comm
    }
    return render(request, "commentview.html", context)
    
def delete(request, id):
    com=comment.objects.get(id=id)
    com.delete()
    return redirect('/newsportal/')
    
def edit(request, id):
    com=comment.objects.get(id=id)
    return render(request, 'edit.html',{'com':com})
    
def updatecomment(request,id):
    com=comment.objects.get(id=id)
    form=commentform(request.POST, instance=com)
    if form.is_valid():
        form.save()
        return redirect('/newsportal/')
    return render(request,'edit.html',{'com':com})

def addnewsview(request):
      cat=category.objects.all()
      return render(request,"addnews.html",{'cat':cat})

def insertnews(request):
    if request.method=='POST':
        form=newsform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'News added successfully!')
                return redirect('/addnews/')
            except:
                pass
        else:
             messages.warning(request, 'Please correct the error below.')
    else:
        form=newsform()
    return render(request,'addnews.html',{'form':form})    
    