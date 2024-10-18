from django.urls import path
from .views import UserRegisterAPI, PostAPI, PostDetailsAPI


urlpatterns = [
    path('user/', UserRegisterAPI.as_view()),
    path('posts/', PostAPI.as_view()),
    path('posts/<pk>/', PostDetailsAPI.as_view()),
]