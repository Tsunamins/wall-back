from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message

class UserSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'messages']

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Message
        fields = ('id', 'content', 'user', 'created_at', 'updated_at')