from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    content = models.CharField(max_length=250)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



