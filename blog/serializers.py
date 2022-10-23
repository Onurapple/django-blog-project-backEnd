from dataclasses import fields
from rest_framework import serializers
from .models import Comment, Like, Post, PostView



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
   

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
    
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    postview_count = serializers.SerializerMethodField()
    like = LikeSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    postview = PostViewSerializer(many=True, read_only=True)
    #author = serializers.CharField(source='author.email', read_only=True)
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'status',
            'slug',
            'author',
            'like',
            'comment',
            'postview',
            'like_count',
            'comment_count',
            'postview_count'
            ]
   
    def get_like_count(self, obj):
        return Like.objects.filter(post=obj.id).count()
    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj.id).count()
    def get_postview_count(self, obj):
        return PostView.objects.filter(post=obj.id).count()