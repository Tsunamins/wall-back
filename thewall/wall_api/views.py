from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, MessageSerializer
from django.contrib.auth.models import User
from .models import Message

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )
  
class MessageCreateView(CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )
  

class MessageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )

# class MessageDetailView(RetrieveAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = (permissions.AllowAny, )    


# class MessageUpdateView(UpdateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = (permissions.IsAuthenticated, )
#     # permission_classes = (permissions.AllowAny, )


# class MessageDeleteView(DestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     #permission_classes = (permissions.IsAuthenticated, )
#     permission_classes = (permissions.AllowAny, )


