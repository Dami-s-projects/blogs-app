"""Defines the URL patterns for Blogs app"""

from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns=[
    #URL pattern for Homepage
    path('',views.index,name='index'),
    #URL patttern that displays each entry for a blog post
    path('<int:blogposttitle_id>',views.display_contents,name='blog_content'),
    #URL pattern for BLOG headlines page
    path('blog_headlines',views.display_headlines,name="blog_topics"),
    #URL pattern for adding a new topic (blog topic) - Topic form
    path('add_blog_title',views.add_blog_headline,name="add_headline"),
    #path that adds blog contents (Adds Entries to a topic)
    path('content/<int:blogposttitle_id>',views.add_each_content,name="add_each_content"), #(path,view function,template and url name(same name))
    #path that allows user to edit a content they have written before
    path('edit_content/<int:blogcontent_id>',views.edit_an_entry,name="edit_entry"),


]