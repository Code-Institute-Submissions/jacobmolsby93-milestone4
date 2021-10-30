from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from cloudinary.models import CloudinaryField
# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, related_name="member", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    profile_image = CloudinaryField('image', default='default_image')
    description = models.TextField()


    def __str__(self): 
        return f"({self.id})"

    
    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('profile-page', args=[str(self.id)])



@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
    instance.member.save()