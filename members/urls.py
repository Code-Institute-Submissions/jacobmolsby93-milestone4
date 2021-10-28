from . import views
from django.urls import path


urlpatterns = [
    path('profile/<int:pk>', views.profile_page_view, name='profile_page'),
    path('profile/edit/<int:pk>', views.edit_profile, name='edit_profile'),
 ]