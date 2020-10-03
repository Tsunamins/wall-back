
from django.contrib import admin
from django.urls import path, include

from allauth.account.views import ConfirmEmailView
from . import views


urlpatterns = [
    # standard urls
    path('non-admin/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # rest-auth pkg urls
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # api
    path('wall-api/', include('wall_api.urls')),
    # email confirmations
    path('account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    path('account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('complete/$', views.complete_view, name='account_confirm_complete'),
  
]
