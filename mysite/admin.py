from django.contrib import admin

# Register your models here.


from . import models

class RegisteredUser(admin.ModelAdmin):
	list_display = ('name','email','Pcode','referred_by','pub_date')

class UserRandomMapping(admin.ModelAdmin):
	list_display = ('user','random_text','created_at')

class CompletedUser(admin.ModelAdmin):
	list_display = ('user','coins','coins_sent','created_at')

admin.site.register(models.RegisteredUser, RegisteredUser)
admin.site.register(models.UserRandomMapping, UserRandomMapping)
admin.site.register(models.CompletedUser, CompletedUser)
