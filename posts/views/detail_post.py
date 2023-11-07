from requests import Response
from posts.models import Post
from rest_framework import generics
from posts.serialozers import PostSerialazer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer
   