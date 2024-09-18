from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm  # You'll need to create this form

def post_list(request):
    """
    Display a list of all posts.

    **Context**
    - 'posts': A QuerySet of all available Post objects.

    **Template**
    - 'difficulties/post_list.html'
    """
    posts = Post.objects.filter(status=1)  # Fetch all published posts
    return render(request, 'difficulties/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    """
    Display details for a specific post, including its comments.

    **Context**
    - 'post': The selected Post instance.
    - 'comments': A QuerySet of Comment objects related to the post.

    **Template**
    - 'difficulties/post_detail.html'
    """
    post = get_object_or_404(Post, id=post_id, status=1)  # Get the specific published post or 404
    comments = post.comments.filter(approved=True)  # Get all approved comments related to the post
    return render(request, 'difficulties/post_detail.html', {'post': post, 'comments': comments})

def submit_comment(request, post_id):
    """
    Allow users to submit comments for a post.

    **Context**
    - 'form': A CommentForm instance for user input.
    - 'post': The Post instance being commented on.

    **Template**
    - 'difficulties/submit_comment.html'
    """
    post = get_object_or_404(Post, id=post_id, status=1)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Assuming you're using authentication
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'difficulties/submit_comment.html', {'form': form, 'post': post})