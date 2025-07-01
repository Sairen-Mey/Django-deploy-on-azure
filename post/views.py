from .models import Post, Image, Tag, PostTag
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post/posts_list.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet, need to add author
            post.author = request.user
            post.save()
            images = form.files.getlist("images")
            for img in images:
                Image.objects.create(post=post, image=img)
            return redirect('post:post_list')  # Redirect to a list of posts
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})






def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post:post_list')
    return render(request, 'post/successful_deletion.html', {'post': post})


def post_edit(request):
    pass
