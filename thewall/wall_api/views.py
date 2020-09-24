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

from django.core.mail import send_mail

from .serializers import UserSerializer, MessageSerializer
from django.contrib.auth.models import User
from .models import Message

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # will have to wait for registration to add, so can incorporate into
    # send_mail('Welcome to the Wall', 'Login and write your first message on the wall', 'reillyamr@gmail.com', ['reillyamr@gmail.com'], fail_silently=False)


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


