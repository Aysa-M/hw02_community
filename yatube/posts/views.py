from django.shortcuts import get_object_or_404, render

from .models import Group, Post


# Create your views here.
def index(request):
    """Information which is showing up on the start page."""
    text = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': text,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Information for displaying on the page with posts grouped by GROUPS."""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
