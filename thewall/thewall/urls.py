
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('non-admin/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    path('wall-api/', include('wall_api.urls'))
]
