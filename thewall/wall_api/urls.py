from django.urls import path
from .views import (
    UserList,
    UserDetail,
    MessageListView,
   # MessageDetailView,
    MessageCreateView,
   # MessageUpdateView,
   # MessageDeleteView,
    MessageRetrieveUpdateDestroyView
  
)

urlpatterns = [
 path('users/', UserList.as_view()),
 path('users/<int:pk>/', UserDetail.as_view()),
 path('messages/', MessageListView.as_view()),
 path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view()),
 path('messages/create/', MessageCreateView.as_view()),
 path('messages/<int:pk>/update/', MessageRetrieveUpdateDestroyView.as_view()),
 path('messages/<int:pk>/delete/', MessageRetrieveUpdateDestroyView.as_view()),
 
]