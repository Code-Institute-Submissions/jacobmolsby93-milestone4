from django.db import models
from members.models import Member
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Article(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, related_name='article_post')
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='article_like', blank=True)


    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_urls(self):
        return reverse('home')