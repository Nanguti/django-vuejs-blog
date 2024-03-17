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
from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


from rest_framework.pagination import PageNumberPagination

class LatestPostsPagination(PageNumberPagination):
    page_size = 6

class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class LatestPosts(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[0:4]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostList(viewsets.ModelViewSet):

    paginator = LatestPostsPagination()
    queryset = Post.objects.select_related('category').prefetch_related('comments', 'tag_set') 
    serializer_class = PostSerializer
    filter_backends = [OrderingFilter]
    ordering = ['-published_date'] 
    pagination_class = LatestPostsPagination

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def search(self, request):
        query = request.query_params.get('q')
        if query:
            queryset = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response([])
        
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        query = request.query_params.get('q')
        if query:
            queryset = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)




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
