from .models import Post, PostImage, Tag, PostTag
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from PIL import Image as PilImage
from django.http import HttpResponse
from io import BytesIO
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
            images = form.cleaned_data["images"]
            if not images:
                print("Error")
            for img in images:
                i = PostImage.objects.create(post=post, image=img)
                print(i.image.url)
            return redirect('user:profile', username=post.author.username)  # Redirect to a list of posts
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})






def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('user:profile', username=post.author.username)
    return render(request, 'post/successful_deletion.html', {'post': post})


def thumbnail_view(request, post_pk, image_pk):
    img_obj = get_object_or_404(PostImage, pk=image_pk, post_id=post_pk)
    img = PilImage.open(img_obj.image.path)
    img = img.convert('RGB')
    img.thumbnail((300, 300), PilImage.Resampling.LANCZOS)

    buf = BytesIO()
    img.save(
        buf,
        format='JPEG',
        quality=90,
        optimize=True,
        progressive=True
    )

    return HttpResponse(buf.getvalue(), content_type='image/jpeg')

def post_edit(request):
    pass
