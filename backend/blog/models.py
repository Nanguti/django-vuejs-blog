from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()


    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    summary = models.TextField()
    content = models.TextField()
    featured_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('-published_date',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Comment(models.Model):
    content = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:20]}..."  # Truncate comment preview

class Tag(models.Model):
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
