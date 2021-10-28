from . import views
from django.urls import path


urlpatterns = [
    path('profile/<int:pk>', views.ProfilePageView.as_view(), name='profile_page'),
 ]