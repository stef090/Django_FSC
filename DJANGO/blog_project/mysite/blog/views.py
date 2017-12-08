from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from blog.forms import PostForm, CommentForm
from django.views.generic import (TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # Since we inherited from LoginRequiredMixin, we need to specify a login url

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request, pk):
    # Get the requested post from the pk
    post = get_object_or_404(Post, pk=pk)
    # Publish the post
    post.publish()
    # Redirect to the post_detail view
    return redirect('post_detail', pk=pk)


##############################################
##############################################
# Comment views


# function based view to add comments to posts
@login_required
def add_comment_to_post(request, pk):
    """

    :param request: Request object
    :param pk: id of the requested post
    :return: redirects to post page if comment is validated,
             else returns the comment form
    """
    # Get the requested Post object
    post = get_object_or_404(Post, pk=pk)
    # If the method of the request is POST, then validate and save the form data.
    # Link the comment to the post and redirect to the post page.
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    # If the method is not POST (most commonly GET) then just return the form
    else:
        form = CommentForm()
    # Render the template for the comment form
    return render(request, 'blog/comment_form.html', {'form': form})

# function based view to approve comments
@login_required
def comment_approve(request, pk):
    # Take in the pk which is the id of the comment up for approval
    comment = get_object_or_404(Comment, pk=pk)
    # Use the approve method of the Comment instance
    comment.approve()
    # Redirect to the post detail page using the name attribute of the view,
    # with the pk being the id of the post that the comment is attached to
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    # Take in the pk which is the id of the comment up for approval
    comment = get_object_or_404(Comment, pk=pk)
    # Save the pk of the post the comment is attached to, for later use in redirect
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
