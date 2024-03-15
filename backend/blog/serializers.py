from rest_framework import serializers
from .models import Post, Category, Comment, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    posted_by_username = serializers.SerializerMethodField()  # To include username if applicable

    def get_posted_by_username(self, obj):
        if obj.posted_by:
            return obj.posted_by.username
        return None

    class Meta:
        model = Comment
        fields = ('id', 'content', 'posted_by_username', 'posted_date')

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    comments = CommentSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'published_date', 'author', 'author_name', 'category', 'category_name', 'comments', 'tags', 'featured_image', 'thumbnail')

    def get_author_name(self, obj):
        return obj.author.username if obj.author else None

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None
