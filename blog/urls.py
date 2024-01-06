from django.urls import path 
from .import views 

urlpatterns = [
    path("", views.starting_page),
    path("posts", views.posts),
    path("posts/<slug>", views.post_details,
         name="post-details-page") # /posts/my-first-post --> concept called Slug
]
