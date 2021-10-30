from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Member
from articles.models import Article
from .forms import ProfileForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


@login_required
def ProfilePageView(request):
    member = None
    try:
        member = request.user.member
    except:
        return redirect('create_profile.html')

    user = request.user

    context = {
        "user": user,
        "member": member
    }
    return render(request, 'profiles/profile_page.html', context)
    


@login_required
def EditProfile(request):
    if request.method == "GET":
        form = ProfileForm(instance=request.user.member)
        context = {"form":form}
        return render(request, 'profiles/edit_profile.html', context)
    if request.method == "POST":
        form = ProfileForm(request.POST or None, instance=request.user.member)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('members:profile_page'))

        context = {"form":form}
        return render(request, 'profiles/edit_profile.html', context)


def LoginView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('articles:home'))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('articles:home'))
        else:
            form = AuthenticationForm()
            return render(request,'login.html',{'form' : form,"message":"Wrong username or password"})

    form = AuthenticationForm()
    return render(request,'login.html',{'form' : form})

def SignUpView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('articles:home'))

    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        member_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and member_form.is_valid():

            user = user_form.save()
            
            user.refresh_from_db()
            
            first_name = member_form.cleaned_data.get('first_name', None)
            last_name = member_form.cleaned_data.get('last_name', None)
            email = member_form.cleaned_data.get('email', None)
            profile_image = request.FILES.get('profile_image', None)
            description = member_form.cleaned_data.get('description', None)

            user.member.first_name = first_name
            user.member.last_name = last_name
            user.member.email = email
            user.member.profile_image = profile_image
            print(
                profile_image
            )
            user.member.description = description

            user.member.save()

            if user is not None:

                login(request, user)
                return HttpResponseRedirect(reverse('articles:home'))
        else:
            user_form = UserCreationForm(request.POST)
            member_form = ProfileForm(request.POST, request.FILES)
            context = {"member_form": member_form, "user_form": user_form}
            return render(request, 'signup.html', context)

    member_form = ProfileForm()
    user_form = UserCreationForm()
    context = {"member_form": member_form, "user_form": user_form}
    return render(request, 'signup.html', context)
    