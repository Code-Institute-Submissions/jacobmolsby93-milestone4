from django.views.generic import ListView, DetailView
from django.views import generic
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from .models import Member
from articles.models import Article 

# Create your views here.


class ProfilePageView(generic.ListView):
    """
    generic class-based view for a list of blogs posted by a user
    """
    model = Article
    paginate_by = 5
    template_name ='profiles/profile_page.html'
    
    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author = get_object_or_404(Member, pk = id)
        return Member.objects.filter(user=target_author)
        
    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['Blogger'] = get_object_or_404(Member, pk = self.kwargs['pk'])
        return context
    
