from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('loans/', include('loans.urls')),
    path('admins/', include('admins.urls')),
]
