from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from posts.models import Post


class DeletePost(View):
    def get(self, request, _id):
        post = Post.objects.get(id=_id)
        post.delete() 
        return HttpResponse('Пост удален')