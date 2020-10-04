from django.urls import path
from .views import (
    UserList,
    UserDetail,
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    CurrentUserView
  
)

urlpatterns = [
 path('users/', UserList.as_view()),
 path('users/<int:pk>/', UserDetail.as_view()),
 path('users/get-current-user/', CurrentUserView.as_view()),
 path('messages/', MessageListView.as_view()),
 path('messages/<int:pk>/', MessageDetailView.as_view()),
 path('messages/create/', MessageCreateView.as_view()),
 path('messages/<int:pk>/update/', MessageUpdateView.as_view()),
 path('messages/<int:pk>/delete/', MessageDeleteView.as_view()),
 
]