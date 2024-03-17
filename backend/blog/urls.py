from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet


from . import views

router = DefaultRouter()
router.register(r'posts', views.PostList, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentList, basename='comments') 
router.register(r'search', PostViewSet, basename='posts-search')

urlpatterns = [
    path('', include(router.urls)),
    path('categories', views.Categories.as_view(), name='categories'), 
    path('comments', views.CommentCreate.as_view(), name='comment-create'),
    path('tags', views.TagList.as_view(), name='tags'),
]
