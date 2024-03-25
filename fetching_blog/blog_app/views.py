from django.shortcuts import render
from blog_app.models import BlogPostTable
import requests

def load_blog_post(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    if response.status_code == 200:
        blog_posts_data = response.json()
        for post_data in blog_posts_data:
            BlogPostTable.objects.update_or_create(
                userId=post_data['userId'],
                id=post_data['id'],
                title=post_data['title'],
                body=post_data['body']
            )
        
        blog_posts = BlogPostTable.objects.all()
        return render(request, 'blog_app/blog_posts.html', {'blog_posts': blog_posts})
    else:
        return HttpResponse('Failed to fetch blog posts from the external API')
            


# def fetch_posts_view(request):
#     call_command('loading_data')
#     return HttpResponse('Fetching blog posts...')