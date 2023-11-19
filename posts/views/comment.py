from posts.models import Comment
from rest_framework import generics
from posts.serialozers import CommentSerialazer
from rest_framework.permissions import IsAuthenticated



class CommentView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerialazer
    