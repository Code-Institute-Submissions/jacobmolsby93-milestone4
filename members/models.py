from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
# Create your models here.

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    profile_image = CloudinaryField('profile_image', default='profile_image')
    description = models.TextField()
    id = models.BigAutoField(primary_key=True)

    def __str_(self): 
        return self.id + self.email
    