def post_image_upload_path(instance, file_name):
    return f'posts/user_{instance.post.author.id}/{file_name}'