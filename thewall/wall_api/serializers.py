from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'messages']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('content', 'created_at', 'updated_at')