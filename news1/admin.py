from django.contrib import admin
from news1.models import *

@admin.register(category)
class categoryadmin(admin.ModelAdmin):
	pass
	
@admin.register(news)
class newsadmin(admin.ModelAdmin):
	list_display=['title','userid','status']	
	list_filter=['status','tag','userid','category']

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
	list_display=('name','email','phone','comments','suggestion','experience',)


@admin.register(videonews)
class videonewsadmin(admin.ModelAdmin):
	pass

# Register your models here.
