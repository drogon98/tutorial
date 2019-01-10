from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import (
       RegistrationForm,
       EditProfileForm,
       )
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form=RegistrationForm()
    return render(request,"accounts/register.html",{'form':form})



def profile(request,pk=None):# the request has access to many of the user objects
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    context={'user':user}
    return render(request,"accounts/profile.html",context)




def edit_profile(request):
    if request.method=="POST":
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:profile"))
    else:
        form=EditProfileForm(instance=request.user)
    return render(request,"accounts/prof_edit.html",{"form":form})




def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponseRedirect(reverse("accounts:profile"))
        else:
            return HttpResponseRedirect(reverse("accounts:change_password"))
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,"accounts/pass_change.html",{"form":form})
