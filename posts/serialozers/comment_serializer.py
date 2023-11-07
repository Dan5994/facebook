from posts.models import Comment
from rest_framework import serializers

class CommentSerialazer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only = True)
    status = serializers.CharField(read_only = True)
    post_id_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance