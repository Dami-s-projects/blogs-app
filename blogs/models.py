from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPostTitle(models.Model):
    """Class to represent list of blog headlines"""
    text=models.CharField(max_length=250)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the blog post title"""
        return self.text
    
class BlogContent(models.Model):
    """Class to represent the content page of a blog.
    This is the page connected to a blog title"""
    blog_post_title=models.ForeignKey(BlogPostTitle,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural= 'entries'
    
    def __str__(self):
        """Returns a short representation of blog contents when needed"""
        if len(self.text)<50:       
            return self.text
        else:
            return self.text[:50] + "..."

