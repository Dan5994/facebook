from requests import Response
from posts.models import Post
from rest_framework import generics
from posts.serialozers import PostSerialazer
from rest_framework.permissions import IsAuthenticated


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerialazer
   