from rest_framework import generics
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAuthorOrReadOnly

class UserRegisterAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PostDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]

