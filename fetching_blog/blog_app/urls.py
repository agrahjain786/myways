from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.load_blog_post, name='load_blog_post'),
]