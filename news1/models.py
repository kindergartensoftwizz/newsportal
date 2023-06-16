from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

class contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	comments=models.CharField(max_length=200)
	suggestion=models.CharField(max_length=200)
	experience=models.CharField(max_length=200)
	
	
	class Meta:
		db_table="contact"		
		
class category(models.Model):
	name=models.CharField(max_length=200)		
	image=models.ImageField(upload_to = 'image/')
	class Meta:
		db_table="category"
	def __str__(self):
		return self.name
		
		
class news(models.Model):
	title=models.CharField(max_length=200)		
	category=models.ForeignKey(category,on_delete=models.CASCADE)
	description=HTMLField()	
	image=models.ImageField(upload_to = 'image/')	
	postby=models.CharField(max_length=200)		
	poston=models.CharField(max_length=200)		  
	TAG_CHOICES = (
		('new','NEW'),
		('Breaking','BREAKING'),
		('recent','RECENT'),
		('latest','LATEST'),
	)
	STATUSCHOICE=(
		('active','active'),
		('inactive','inactive')
	)
	tag = models.CharField(max_length=10, choices=TAG_CHOICES, default='new')	
	userid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default="1")
	status=models.CharField(max_length=20,default="active",choices=STATUSCHOICE)

	class Meta:
		db_table="news"
	def __str__(self):
		return f"{self.title}--{self.status}--{self.userid}"
		
		
class videonews(models.Model):
	title=models.TextField()	
	link=models.CharField(max_length=300)
	categoryid=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)
	class Meta:
		db_table="videonews"
	def __str__(self):
		return self.title


class comment(models.Model):
    comment=models.TextField()
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    newsid=models.ForeignKey(news, on_delete=models.CASCADE, default="")
    class Meta:
        db_table='comment'		
		
		
		
		
		
		
		
		
'''class Headline(models.Model):
	title = models.CharField(max_length=200)
	image = models.URLField(null=True, blank=True)
	url = models.TextField()
	
 currentdate= models.DateField(default=timezone.now)
	
	def __str__(self):
		return self.title		'''