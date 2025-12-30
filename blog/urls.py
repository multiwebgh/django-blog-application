from django.urls import path
from blog import views


urlpatterns = [
    path('', views.BlogListFunc, name = "home_link" ),
     path('blog/create/', views.CreatePostFunc, name='create_link'),
     path('blog/my-posts/', views.MyPostsFunc, name='my_posts_link'),
     path('blog/<slug:slug>/like/', views.like_blog, name="like_blog"),
     path('blog/<slug:slug>/',  views.BlogDetailsFunc, name = "details_link" ),
     
     ]


