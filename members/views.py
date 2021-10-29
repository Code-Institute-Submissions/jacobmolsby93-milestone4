from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Member
from articles.models import Article
from .forms import ProfileForm, EditProfileForm


def profile_page_view(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        member = Member.objects.get(pk=pk)
        article = Article.objects.filter(status=1).order_by('user')

    else:
        user = request.user
    context = {
        'user': user,
        'member': member,
        'article': article
    }
    return render(request, 'profiles/profile_page.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('members:profile_page_view'))
    else:
        form = EditProfileForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'profiles/edit_profile.html', context)