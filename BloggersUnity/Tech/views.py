from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeForm, PasswordResetForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import CustomSignUpForm, UserProfileForm, BlogPostForm, BlogPostEditForm
from .models import BlogPost


def index(request):
    return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        signup_form = CustomSignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('login')
        else:
            pass
    else:
        signup_form = CustomSignUpForm()

    return render(request, 'signup.html', {'signup_form': signup_form})


@login_required
def user_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Profile update failed. Please check the form.')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'user_profile.html', context)


@login_required
def user_blog_posts(request):
    user = request.user
    status = request.GET.get('status', 'published')  # Default to 'published'

    if status == 'published':
        user_posts = BlogPost.objects.filter(author=user, status='published')
    elif status == 'draft':
        user_posts = BlogPost.objects.filter(author=user, status='draft')
    elif status == 'archived':
        user_posts = BlogPost.objects.filter(author=user, status='archived')
    else:
        user_posts = BlogPost.objects.filter(author=user, status='published')

    return render(request, 'user_blog_posts.html', {'user_posts': user_posts})


@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('user_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


@login_required
def edit_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id, author=request.user)

    if request.method == 'POST':
        form = BlogPostEditForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('user_blog_posts')  # Redirect to the list of blog posts

    else:
        form = BlogPostEditForm(instance=blog_post)

    return render(request, 'edit_blog_post.html', {'form': form, 'blog_post': blog_post})


@login_required
def delete_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id, author=request.user)

    if request.method == 'POST':
        blog_post.delete()  # Call the custom delete method
        return redirect('user_blog_posts')  # Redirect to the list of blog posts

    return render(request, 'delete_blog_post.html', {'blog_post': blog_post})


@login_required
# View to publish a blog post
def publish_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    blog_post.status = 'published'
    blog_post.save()
    return redirect('user_blog_posts')  # Redirect to your list of blog posts


@login_required
# View to archive a blog post
def archive_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    blog_post.status = 'archived'
    blog_post.save()
    return redirect('user_blog_posts')  # Redirect to your list of blog posts


@login_required
# View to draft a blog post
def draft_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    blog_post.status = 'draft'
    blog_post.save()
    return redirect('user_blog_posts')  # Redirect to your list of blog posts


# View a Blog Post
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_post_list.html'
    context_object_name = 'blog_posts'
    ordering = ['-pub_date']  # Display posts in descending order of publication date

    def get_queryset(self):
        return BlogPost.objects.filter(status='published').order_by('-pub_date')


def blog_post_detail(request, post_slug):
    # Retrieve the blog post based on the slug
    post = get_object_or_404(BlogPost, slug=post_slug)

    # Now you can pass the 'post' object to your template and render it
    return render(request, 'blog_post_detail.html', {'post': post})


class CustomLoginView(LoginView):
    costom_login = 'login.html'

    def get(self, request, *args, **kwargs):  # Correct the signature
        form = AuthenticationForm()
        return render(request, self.costom_login, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        return render(request, self.costom_login, {'form': form})


class CustomLogoutView(LogoutView):
    next_page = '/'


class CustomPasswordChangeView(LoginRequiredMixin, View):
    template_name = 'password_change.html'

    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('password_change')  # Redirect to a success page or another URL
        else:
            return render(request, self.template_name, {'form': form})


class CustomPasswordResetView(View):
    template_name = 'password_reset.html'

    def get(self, request, *args, **kwargs):
        form = PasswordResetForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Process the password reset logic here
            messages.error(request, "Password reset isn't working. Please contact at example@gmail.com.")
            return redirect('password_reset')  # Redirect to a success page or another URL
