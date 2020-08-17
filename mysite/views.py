from django.shortcuts import render, redirect
from django.http import HttpResponse 
from . import models
from django.db.models import F
import random
import string

def index(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Pubg_id=request.POST.get("pubg_id")
        Reffered_by=request.POST.get("reffered_by")

        if not len(Name):
            return HttpResponse("Name is Required")
        if not len(Email):
            return HttpResponse("Email is Required")
        if not len(Pubg_id):
            return HttpResponse("Pubg id is Required")
       

        query_data = models.RegisteredUser.objects.filter(email=Email).count()
        query_data1 = models.RegisteredUser.objects.filter(Pcode=Pubg_id).count()

        if query_data > 0: #It is checking if query_data is greater than 0.
            return HttpResponse("You have already registered, we found "+str(query_data)+" accounts.") #Then show this information.
        elif query_data1 > 0: 
            return HttpResponse("Pubg_id already exists, Use Another , we found "+str(query_data1)+" accounts.") 
        else: # If no account found.
            register_model = models.RegisteredUser(name=Name,email=Email,Pcode=Pubg_id,referred_by=Reffered_by)
            register_model.save()
            random_text = randomtext(request) # Xy76ru
            random_string_model = models.UserRandomMapping(user=register_model,random_text=random_text) #Createed at - will be added automatically.
            random_string_model.save() 

            if Reffered_by:
                referred_all = models.RegisteredUser.objects.filter(referred_by=Reffered_by)
                if referred_all.count() >= 5:
                    referrer_obj = models.UserRandomMapping.objects.filter(random_text=Reffered_by) 
                    if referrer_obj.count():
                        referrer_obj = referrer_obj[0]
                        CompletedUserData = models.CompletedUser.objects.filter(user=referrer_obj.user)
                        if CompletedUserData.count() == 0:
                            coins = random.randint(10, 15)
                            CompletedUserData = models.CompletedUser(user=referrer_obj.user, coins = coins)
                            CompletedUserData.save()

            return redirect("/"+random_text+"/myprofile")
        return HttpResponse("Some Error Occured")
    
    context = {}
    context['userid'] = "" # Keep it blank only.
    return render(request,'PUBG.html', context)  

def checkprofile(request):
    if request.method=="POST":
        Name=request.POST.get("name")

        if not len(Name):
            return HttpResponse("Email or Pubg ID is Required")
       
        query_data = models.UserRandomMapping.objects.filter(user__email__iexact=Name)

        if query_data.count() > 0: #It is checking if query_data is greater than 0.
            query_data = query_data[0]
            random_text = query_data.random_text
            return redirect("/"+random_text+"/myprofile")

        else: # If no account found.
            query_data1 = models.UserRandomMapping.objects.filter(user__Pcode__iexact=Name)
            if query_data1.count() > 0: #It is checking if query_data is greater than 0.
                query_data1 = query_data1[0]
                random_text = query_data1.random_text
                return redirect("/"+random_text+"/myprofile")
            return HttpResponse("No account found")
    
    return render(request,'checkprofile.html')  

def randomtext(request):
    while True:
        random_text = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 6)) #aaaaaa
        query_data = models.UserRandomMapping.objects.filter(random_text=random_text).count() # If not exst - 0. If exist - 1
        if query_data == 0:
            return random_text #aaaaaa

def referpage(request, userid):
    # Exception Handling - Interview 8 out 10 companies. Try, except, finally, else.
    try:
        userdata = models.UserRandomMapping.objects.get(random_text=userid) # no of row must be 1.
    except:
        return HttpResponse("Incorrect URL")
    context = {}
    context['name'] = userdata.user.name
    context['userid'] = userid # Keep it blank only.
    context['refer'] = True
    return render(request,'PUBG.html', context)  

def referals(request, userid):
    try:
        userdata = models.UserRandomMapping.objects.get(random_text=userid)
    except:
        return HttpResponse("Incorrect URL")
    context = {}
    context['name'] = userdata.user.name
    query_data = models.RegisteredUser.objects.filter(referred_by=userid)
    user_list = []
    for each in query_data:
        user_list.append(each.name)
    count_user =  query_data.count()
    context['count_user'] = count_user
    if count_user >= 5:
        context['rem_user'] = 0
        CompletedUserData = models.CompletedUser.objects.filter(user=userdata.user)
        if CompletedUserData.count():
            comp_user = CompletedUserData[0]
            context['rewards'] = True
            context['coins'] = comp_user.coins
            if comp_user.coins_sent:
                context['coints_sent'] = "Coins Transferred"
            else:
                context['coints_sent'] = "Not transferred yet"
        else:
            return HttpResponse("Some Technical Issue, please mail at mayankgbrc@gmail.com")

    else:
        context['rem_user'] = 5 - count_user
    #userlie = ['ABC','DEF',........]
    context['users'] = user_list
    context['userid'] = userid
    return render(request,'Registered.html', context)

def myprofile(request,userid):
    try:
        userdata = models.UserRandomMapping.objects.get(random_text=userid)
    except:
        return HttpResponse("Incorrect URL")
    context = {}
    context['userid'] = userid
    return render(request,'myprofile.html', context) 