from requests import Response
from posts.models import Post
from rest_framework import generics
from posts.serialozers import PostSerialazer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from posts.filter.filter_post import PostFilter
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from facebook.celery import debug_task

class PostPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialazer
    # permission_classes = [IsAuthenticated]
    @method_decorator(cache_page(60))
    def get(self, request, *args, **kwargs):
        print('Cache')
        debug_task.delay()
        return self.list(request, *args, **kwargs)
    # filter_backends = [PostFilter]
    # filterset_fields = ['cotegoru', 'created_at']
    # pagination_class = PostPagination


    # def get_queryset(self):
    #     counter = self.request.query_params.get('counter')
    #     if counter:
    #         return Post.objects.filter(counter__lte=counter)
    #     return Post.objects.all()
        