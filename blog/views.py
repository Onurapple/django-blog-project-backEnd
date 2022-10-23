from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, PostViewSerializer
from .models import Post, Comment, Like, PostView
from django.shortcuts import get_object_or_404, redirect

class BlogList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.request.user
    #     return super(BlogList, self).create(validated_data)



    # print(Post.objects.count())
    # print(Comment.objects.count())
    # print(Like.objects.count())
    # print(PostView.objects.count())

    

class BlogRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class BlogComment(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    #print(Comment.objects.count())
    # def comment(request, slug):
    #     if request.method == "POST":
    #         obj = get_object_or_404(Post, slug=slug)
    #         like_qs = Comment.objects.filter(user=request.user, post=obj)
            
    #     if like_qs.exists():
    #         like_qs[0].delete()
    #     else:
    #         Comment.objects.create(user=request.user, post=obj)
    #     return redirect("bloglist/", slug=slug)

class BlogLike(generics.ListAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def like(request, slug):
        if request.method == "POST":
            obj = get_object_or_404(Post, slug=slug)
            like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect("bloglist/", slug=slug)




class BlogPostView(generics.RetrieveAPIView):
    serializer_class = PostViewSerializer
    queryset = PostView.objects.all()
    
    


