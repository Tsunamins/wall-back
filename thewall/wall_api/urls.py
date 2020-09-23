from django.urls import path

from .views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    UserList,
    UserDetail
)

urlpatterns = [
 path('users/', UserList.as_view()),
 path('users/<int:pk>/', UserDetail.as_view())
]