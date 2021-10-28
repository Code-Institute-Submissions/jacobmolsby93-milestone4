from django.db import models
from articles.models import Article
from django.urls import reverse

from cloudinary.models import CloudinaryField
# Create your models here.

class Member(models.Model):
    user = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='member')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    profile_image = CloudinaryField('profile_image', default='profile_image')
    description = models.TextField()


    def __str__(self): 
        return f"{self.user.user}"

    
    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('profile-page', args=[str(self.id)])