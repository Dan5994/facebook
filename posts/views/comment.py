from django.views import View
from posts.models import Comment
from django.http import HttpResponse, JsonResponse
import json


class CommentView(View):
    @staticmethod
    def parsing_data(comment:Comment):
        return{'id':comment.id, 'post_id':comment.post_id_id, 'text':comment.text, 'status':comment.status, 'created_at':comment.created_at}
    
    def get(self,request, *args, **kwargs):
        result = {
            'data':[]
        }
        comment = Comment.objects.all()
        for item in comment:
            result['data'].append(self.parsing_data(item))
        return JsonResponse(result)
    
    def post(self, request):
        post_id = json.loads(request.body.decode('utf-8')).get('post_id','')
        text = json.loads(request.body.decode('utf-8')).get('text','')
        comment = Comment(post_id_id=post_id, text=text)
        comment.save()
        return JsonResponse({'id':comment.id, 'text':comment.text, 'post_id':comment.post_id_id})