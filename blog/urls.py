from django.urls import path 
from .import views 

urlpatterns = [
    path("", views.starting_page),
    path("posts", views.posts),
    path("posts/<slug>", views.post_details) # /posts/my-first-post --> concept called Slug
]
