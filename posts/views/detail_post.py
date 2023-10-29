from django.views import View
from posts.models import Post
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json


class DetailPostView(View):
    @staticmethod
    def parsing_data(post:Post):
        return{'id':post.id, 'title':post.title, 'text':post.text, 'counter':post.counter}
    
    def get(self,request,_id):
        post = Post.objects.get(id=_id)
        template = loader.get_template('post/post_detail.html')
        context = {
            'post':post
        }
        return HttpResponse(template.render(context, request))
   
    def delete(self,request,_id):
        post = Post.objects.get(id=_id)
        post.delete()
        return HttpResponse('Post deleted')
    
    def patch(self, request, _id):
        post = Post.objects.get(id=_id)
        title = request.POST.get('title')
        text = request.POST.get('text')
        post.title = title
        post.text = text
        post.save()
        return HttpResponse('Пост обновлен')
    
    def put(self, request, _id):
        post = Post.objects.get(id=_id)
        data = json.loads(request.body.decode('utf-8'))
        post.title = data.get('title','')
        post.text = data.get('text','')
        post.counter = data.get('counter','')
        post.save()
        return HttpResponse('Post update')
    