from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    GenericAPIView
)


from .serializers import UserSerializer, MessageSerializer
from django.contrib.auth.models import User
from .models import Message
from wall_api.permissions import UserLoggedInandMatch


class CurrentUserView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, UserLoggedInandMatch)

    def get(self, request):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)



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
  

class MessageDetailView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )    


class MessageUpdateView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, UserLoggedInandMatch)
 

class MessageDeleteView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, UserLoggedInandMatch)
  


