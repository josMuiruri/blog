from django.shortcuts import get_object_or_4o4, render
from django.http import Http404
from . models import Post


# Create your views here.
def post_detail(request, id):
    post = get_object_or_4o4(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.htlm', {'post': post})
    #try:
    #    post = Post.published.get(id=id)
    #except Post.DoesNotExist:
    #    raise Http404("No Post found.")
    #return render(request, 'blog/post/detail.html', {'post': post})

def post_list(request):
    posts = Post.publish.all()
    return render(request, 'blog/post/list.html', {'post': posts})