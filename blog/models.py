from random import choices
from django.db import models
from django.shortcuts import reverse

class Post(models.Model):

    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    ) #! be sorate tople baraye dadan be status

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)#! neshon dahande zamane sakht post
    datetime_modified = models.DateTimeField(auto_now=True) #! neshon dahande zamanr virayeshe post
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def get_absolute_url(self):
        # return reverse('posts_list') #! in mele safe asli
        return reverse('post_detail', args=[self.id]) #! in mire to detail jadidi ke sakhtin

    # def __str__(self):
    #     return self.title

    

# Create your models here.
