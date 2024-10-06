from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    youtube_title = models.CharField(max_length=300)
    youtube_link = models.URLField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.youtube_title