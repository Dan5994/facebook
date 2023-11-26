from datetime import datetime
from requests import Response
from posts.models import Post
from rest_framework import serializers
from .comment_serializer import CommentSerialazer

class PostSerialazer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    counter = serializers.IntegerField()
    cotegoru = serializers.CharField()
    created_at = serializers.DateTimeField(read_only = True)
    
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.counter = validated_data.get('counter', instance.counter)
        instance.cotegoru = validated_data.get('cotegoru', instance.cotegoru)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance
    
    # def delete(self, request,*args,**kwargs):
    #     pk = kwargs.get("pk", None)
    #     pk.delete()
    #     return Response({'post':'delete post' + str(pk)}) 
