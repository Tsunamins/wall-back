from django.urls import path

from allauth.account.views import ConfirmEmailView
from . import views

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
 
 path('registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
 path('registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
 path('registration/complete/$', views.complete_view, name='account_confirm_complete'),
 path('password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
]