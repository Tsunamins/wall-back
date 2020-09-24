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

from .serializers import UserSerializer, MessageSerializer
from django.contrib.auth.models import User
from .models import Message

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
    # permission_classes = (permissions.AllowAny, )

class MessageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )

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


