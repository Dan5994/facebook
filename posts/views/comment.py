from posts.models import Comment
from rest_framework import generics
from posts.serialozers import CommentSerialazer



class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialazer
    