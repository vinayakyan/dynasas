from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('blog.urls')),
    path('token/', obtain_auth_token),
]
