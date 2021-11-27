from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm, ProfileUpdateForm
# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f" Your profile has been updated")
            return redirect('profileView')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html',context) 


@login_required
def profileView(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request, 'user/profileview.html',context)



def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}  ")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html',{'form':form}) 

