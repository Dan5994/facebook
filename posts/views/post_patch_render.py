from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from posts.models import Post


class EditFormRender(View):
    def get(self, request, _id):
        post = Post.objects.get(id=_id)
        form_created = render(request, 'post/patch_post.html', {'_id': post.id})
        return HttpResponse(form_created)