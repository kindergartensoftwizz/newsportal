from django import forms
from news1.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
	
			
class contactform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	comments=forms.CharField(max_length=200)
	suggestion=forms.CharField(max_length=200)
	experience=forms.CharField(max_length=200)
	
	
	class Meta:
		model=contact
		fields="__all__"
			

class videonewsform(forms.ModelForm):
	class Meta:
		model=videonews
		fields='__all__'			
		
class signform(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2',)

class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields='__all__'

class newsform(forms.ModelForm):
	class Meta:
		model=news
		fields='__all__'