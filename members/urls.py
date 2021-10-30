from . import views
from django.urls import path

app_name="members"

urlpatterns = [
    path('profile/', views.ProfilePageView, name='profile_page'),
    path('profile/edit/', views.EditProfile, name='edit_profile'),
    path('login/', views.LoginView, name='LoginView'),
    path('signup/', views.SignUpView, name='SignUpView'),
 ]