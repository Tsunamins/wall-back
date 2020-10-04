from rest_framework import permissions
from django.contrib.auth.models import User

class UserLoggedInandMatch(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # kept prints for note to self purposes
        # print('shows article id number:')
        # print(view.kwargs)
        # print('shows current user/logged in')
        # print(request.user)
        # print('shows user of message')
        # print(obj.user)
        # print(request.user == obj.user)
        if request.user == obj.user:
            return True
        return False
