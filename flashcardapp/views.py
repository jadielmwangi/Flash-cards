# from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .email import send_welcome_email


import datetime as dt
from . forms import ProfileForm


# Create your views here.




def index(request):
    date =dt.date.today()
    # posts = Post.objects.all()
    # return render(request, 'projects/index.html', {"date":date, "posts":posts })

    return render(request, 'projects/index.html', {"date":date })

@login_required(login_url='/accounts/login/?next=/')
def profile(request):
    current_user = request.user
   
    profile = Profile.objects.filter(user=current_user).first()
    posts = request.user.post_set.all()

    return render(request, 'projects/profile.html', locals())

@login_required(login_url='/accounts/login/?next=/')
def updateprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = current_user
            add.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'projects/profile_update.html',{"form":form })

