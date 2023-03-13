from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('websocket/', include('websocket.urls')),
    path('api/v1/user/', include('user.urls')),
]
