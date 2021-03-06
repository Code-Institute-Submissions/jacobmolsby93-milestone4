from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from cloudinary.models import CloudinaryField
from django.urls import reverse

from .utils import slugify_instance_title

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='article')
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    featured_image = CloudinaryField('article_image', default='placeholder')
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
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            slugify_instance_title(self, save=False)
        super().save(*args, **kwargs)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Article)



class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body[:50]} by {self.name}"
