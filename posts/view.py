from django.shortcuts import render
from django.views import View
from posts.models import Post, Comment
from django.http import HttpResponse, JsonResponse
from django.db import transaction
import json

# Create your views here.
def posts_comment(request,_id):
    comments = Post.objects.get(id=_id).comments.all()
    result = []
    for comment in comments:
        result.append({'id':comment.id, 'text': comment.text, 'post_id':comment.post_id_id})
    return JsonResponse({'comments':result})

def update_statu(request, _id, status):
        comment = Comment.objects.filter(id=_id).update(status=status)
        return HttpResponse('Post update')


def update_counter(request):
     with transaction.atomic():
        post_1= json.loads(request.body.decode('utf-8')).get('id_1','')
        post_2= json.loads(request.body.decode('utf-8')).get('id_2','')
        cou_1= json.loads(request.body.decode('utf-8')).get('cou_1','')
        cou_2= json.loads(request.body.decode('utf-8')).get('cou_2','')
        tr_1 = Post.objects.filter(id=post_1).update(counter=cou_1)
        2/0
        tr_2 = Post.objects.filter(id=post_2).update(counter=cou_2)
        return HttpResponse('Transaction complete')
     
    #  https://api.open-meteo.com/v1/forecast?latitude=53.9&longitude=27.56&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FMoscow&start_date=${start_date}&end_date=${end_date}