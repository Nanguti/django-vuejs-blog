from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter
from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Post, Comment, Tag
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, TagSerializer


class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class LatestPosts(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[0:4]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostList(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('category').prefetch_related('comments', 'tag_set')  
    serializer_class = PostSerializer
    filter_backends = [OrderingFilter]
    ordering = ['-published_date']  

class PostDetail(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('category').prefetch_related('comments', 'tag_set')
    serializer_class = PostSerializer

class CommentList(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Filter comments by post ID from URL parameter
        post_id = self.kwargs.get('pk')
        return Comment.objects.filter(post_id=post_id)

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
