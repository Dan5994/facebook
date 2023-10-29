from django.views import View
from posts.models import Comment, Post
from django.http import HttpResponse, JsonResponse
import json


class DetailCommentView(View):
    @staticmethod
    def parsing_data(comment:Comment):
        return{'id':comment.id, 'post_id':comment.post_id_id, 'text':comment.text}
    
    def get(self,request,_id):
        comment = Comment.objects.get(id=_id)
        return JsonResponse(self.parsing_data(comment))
    
    def delete(self, request, _id):
        comment = Comment.objects.get(id=_id)
        comment.delete()
        return HttpResponse('Comment deleted')
    
    def patch(self, request, _id):
        comment = Comment.objects.get(id=_id)
        data = json.loads(request.body.decode('utf-8'))
        comment.text = data.get('text','')
        comment.save()
        return HttpResponse('Post update')
    
    def put(self, request, _id):
        comment = Comment.objects.get(id=_id)
        data = json.loads(request.body.decode('utf-8'))
        comment.text = data.get('text','')
        comment.save()
        return HttpResponse('Post update')
    
