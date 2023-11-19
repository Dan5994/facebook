import json

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views import View

from posts.models import Post


class EditPostView(View):

    def post(self, request, _id):
        post = Post.objects.get(id=_id)
        title = request.POST.get('title')
        text = request.POST.get('text')
        post.title = title
        post.text = text
        post.save()
        return HttpResponse('Пост обновлен')