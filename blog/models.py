from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .utils import get_random_code




def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Post(models.Model):
    OPTIONS = [
        ("DR", 'Draft'),
        ("PUB", 'Published'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='default.png', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=OPTIONS, default="PUB", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    # @receiver(pre_save, sender=Post)
    # def pre_save_create_slug(sender, instance, *args, **kwargs):
    #     if instance.slug:
    #         return 
    #     instance.slug = slugify(instance.title + " " + get_random_code())

    # def get_comment_count(self):
    #     return self.comment_set.all().count()
    
    # def get_view_count(self):
    #     return self.postview_set.all().count()
    
    # def get_like_count(self):
    #     return self.like_set.all().count()
    
    # def comments(self):
    #     return self.comment_set.all()

    # def likes(self):
    #     return self.comment_set.all()

    # def postview(self):
    #     return self.comment_set.all()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
   
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
    
    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postview')
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
