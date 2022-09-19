from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
user=get_user_model()
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    id_user=models.IntegerField(null=True)
    bio=models.TextField(blank=True)
    picture=models.ImageField(upload_to='profile_pictures' ,default='wink.png')
    location=models.CharField(max_length=100,blank=True)
    work=models.CharField(max_length=100,blank=True)
    relationship=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id=models.UUIDField(primary_key=True)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images')
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user


