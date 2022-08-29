from django.db import models
from django.contrib.auth import get_user_model
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



