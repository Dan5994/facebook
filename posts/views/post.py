from posts.models import Post
from rest_framework import generics
from posts.serialozers import PostSerialazer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from posts.filter.filter_post import PostFilter
from rest_framework.permissions import IsAuthenticated

class PostPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerialazer
    # filter_backends = [PostFilter]
    # filterset_fields = ['cotegoru', 'created_at']
    # pagination_class = PostPagination


    # def get_queryset(self):
    #     counter = self.request.query_params.get('counter')
    #     if counter:
    #         return Post.objects.filter(counter__lte=counter)
    #     return Post.objects.all()
        