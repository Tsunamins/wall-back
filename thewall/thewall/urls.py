
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('non-admin/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('wall-api/', include('wall_api.urls'))
]
