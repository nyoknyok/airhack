from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    #sender가 군번역할이네..
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', default='null')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
	
    password = models.CharField(max_length=100, default='null')
    name = models.CharField(max_length=100, default='null')
    gender = models.CharField(max_length=100, default='null')
    area = models.CharField(max_length=100, default='null')
    classes = models.CharField(max_length=100, default='null')
    images = models.ImageField(default='null')
    age = models.IntegerField(default=0)
    education = models.CharField(max_length=100, default='null')
    carrer = models.CharField(max_length=100, default='null')
    interests = models.CharField(max_length=100, default='null')
    
    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)


