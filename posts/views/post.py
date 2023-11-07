from posts.models import Post
from rest_framework import generics
from posts.serialozers import PostSerialazer



class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer
    
        
        