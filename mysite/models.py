import datetime
from django.db import models
from django.utils import timezone




class RegisteredUser(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    Pcode = models.CharField(max_length=100)
    referred_by = models.CharField(max_length=128, blank=True, null=True)
    pub_date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Pcode
   

class UserRandomMapping(models.Model):
	user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
	random_text = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)

class CompletedUser(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    coins_sent=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    

    
















'''    
class Choice(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''   
               


