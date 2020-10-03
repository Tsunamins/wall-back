from rest_framework import permissions
from django.contrib.auth.models import User

class UserLoggedInandMatch(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # can write custom code
        print('shows article id number:')
        print(view.kwargs) # shows article id number
        print('shows current user/logged in')
        print(request.user) # shows current username
        print('shows user of message')
        print(obj.user)
        print(request.user == obj.user)
        if request.user == obj.user:
            return True
        return False
