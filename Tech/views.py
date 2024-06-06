# Import necessary modules and classes from Django and your project
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import View

# Import your custom forms and models
from .forms import (
    CustomSignUpForm,
    UserProfileForm,
    BlogPostForm,
    BlogPostEditForm,
    ContactForm,
)
from .models import CustomUser, BlogPost


class HomeView(View):
    """
    Displays the home page with a list of blog posts.

    Attributes:
        template_name (str): The HTML template used for rendering the home page.

    Methods:
        get(request): Handles GET requests for displaying the home page.
    """

    template_name = "Tech/home.html"

    def get(self, request):
        blog_posts = BlogPost.objects.all().order_by("-pub_date")

        context = {
            "blog_posts": blog_posts,
        }

        return render(request, self.template_name, context)


class AboutView(View):
    """
    Displays the 'About' page.

    Methods:
        get(request): Handles GET requests for displaying the 'About' page.
    """

    def get(self, request):
        return render(request, "Tech/about.html")


class ContactView(View):
    """
    Displays the contact page and handles contact form submissions.

    Attributes:
        template_name (str): The HTML template used for rendering the contact page.

    Methods:
        get(request): Handles GET requests for displaying the contact page.
        post(request): Handles POST requests for processing contact form submissions.
    """

    template_name = "Tech/contact.html"

    def get(self, request):
        form = ContactForm()
        return render(
            request, self.template_name, {"form": form, "success_message": ""}
        )

    def post(self, request):
        form = ContactForm(request.POST)

        success_message = ""

        if form.is_valid():
            form.save()
            success_message = (
                "Thank you for your message! We'll get in touch with you shortly."
            )
        else:
            form = ContactForm()

        return render(
            request,
            self.template_name,
            {"form": form, "success_message": success_message},
        )


class FaqsView(View):
    """
    Displays the frequently asked questions (FAQs) page.

    Methods:
        get(request): Handles GET requests for displaying the FAQs page.
    """

    def get(self, request):
        return render(request, "Tech/faqs.html")


class PrivacyPolicyView(View):
    """
    Displays the privacy policy page.

    Methods:
        get(request): Handles GET requests for displaying the privacy policy page.
    """

    def get(self, request):
        return render(request, "Tech/privacy_policy.html")


class SignupView(View):
    """
    Displays the signup page and handles user registration.

    Attributes:
        template_name (str): The HTML template used for rendering the signup page.
        form_class (class): The form class for user registration.

    Methods:
        get(request): Handles GET requests for displaying the signup page.
        post(request): Handles POST requests for user registration and form submissions.
    """

    template_name = "Tech/signup.html"

    form_class = CustomSignUpForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"signup_form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        else:
            # Handle the case where the form is not valid
            return render(request, self.template_name, {"signup_form": form})


class CustomLoginView(LoginView):
    """
    Handles user login and displays the login page.

    Attributes:
        template_name (str): The HTML template used for rendering the login page.

    Methods:
        get(request, *args, **kwargs): Handles GET requests for displaying the login page.
        post(request, *args, **kwargs): Handles POST requests for user login and form submissions.
    """

    template_name = "Tech/login.html"

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        return render(request, self.template_name, {"form": form})


class CustomLogoutView(LogoutView):
    """
    Handles user logout.

    Attributes:
        next_page (str): The URL to redirect to after successful logout.

    Methods:
        (Inherits LogoutView's methods)
    """

    next_page = "/"


class UserProfileView(LoginRequiredMixin, View):
    """
    Displays the user profile page and handles user profile updates.

    Attributes:
        template_name (str): The HTML template used for rendering the user profile page.

    Methods:
        get(request): Handles GET requests for displaying the user profile page.
        post(request): Handles POST requests for user profile updates and form submissions.
    """

    template_name = "Tech/user_profile.html"

    def get(self, request):
        user = request.user
        form = UserProfileForm(instance=user)
        return render(request, self.template_name, {"user": user, "form": form})

    def post(self, request):
        user = request.user
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("user_profile")
        else:
            messages.error(request, "Profile update failed. Please check the form.")
        return render(request, self.template_name, {"user": user, "form": form})


class DashboardView(LoginRequiredMixin, View):
    """
    Displays the user dashboard and handles sorting and filtering of user's blog posts.

    Attributes:
        template_name (str): The HTML template used for rendering the user dashboard.
        per_page (int): Number of blog posts to display per page.

    Methods:
        get(request): Handles GET requests for displaying the user dashboard.
    """

    template_name = "Tech/dashboard.html"
    per_page = 10

    def get(self, request):
        sort = request.GET.get("sort", "newest")  # Default to 'newest'
        user = request.user
        user_posts = BlogPost.objects.filter(author=user).all()

        if sort == "oldest":
            user_posts = user_posts.order_by("pub_date")
        else:
            user_posts = user_posts.order_by("-pub_date")

        status = request.GET.get("status", "all")  # Default to 'all'
        if status != "all":
            user_posts = user_posts.filter(status=status)

        category = request.GET.get("category", "all")  # Default to 'all'
        if category != "all":
            user_posts = user_posts.filter(categories=category)

        user_post_count = user_posts.count()  # For count User post

        paginator = Paginator(user_posts, self.per_page)
        page = request.GET.get("page")

        try:
            user_posts = paginator.page(page)
        except PageNotAnInteger:
            user_posts = paginator.page(1)
        except EmptyPage:
            user_posts = paginator.page(paginator.num_pages)

        context = {
            "user_posts": user_posts,
            "status": status,
            "category": category,
            "user_post_count": user_post_count,
            "sort": sort,
        }

        return render(request, self.template_name, context)


class CreateBlogPostView(LoginRequiredMixin, View):
    """
    Handles the creation of new blog posts.

    Attributes:
        template_name (str): The HTML template used for rendering the create blog post page.

    Methods:
        get(request): Handles GET requests for displaying the create blog post page.
        post(request): Handles POST requests for creating new blog posts.
    """

    template_name = "Tech/create_blog_post.html"

    def get(self, request):
        form = BlogPostForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()

            return redirect("Tech/dashboard")


class EditBlogPostView(LoginRequiredMixin, View):
    """
    Handles the editing of existing blog posts.

    Attributes:
        template_name (str): The HTML template used for rendering the edit blog post page.

    Methods:
        get(request, blog_post_id): Handles GET requests for displaying the edit blog post page.
        post(request, blog_post_id): Handles POST requests for editing existing blog posts.
    """

    template_name = "Tech/edit_blog_post.html"

    def get(self, request, blog_post_id):
        blog_post = get_object_or_404(BlogPost, id=blog_post_id, author=request.user)
        form = BlogPostEditForm(instance=blog_post)

        return render(
            request, self.template_name, {"form": form, "blog_post": blog_post}
        )

    def post(self, request, blog_post_id):
        blog_post = get_object_or_404(BlogPost, id=blog_post_id, author=request.user)
        form = BlogPostEditForm(request.POST, request.FILES, instance=blog_post)

        if form.is_valid():
            form.save()

            return redirect("dashboard")


class DeleteBlogPostView(LoginRequiredMixin, View):
    """
    Handles the deletion of existing blog posts.

    Attributes:
        template_name (str): The HTML template used for rendering the delete blog post page.

    Methods:
        get(request, blog_post_id): Handles GET requests for displaying the delete blog post page.
        post(request, blog_post_id): Handles POST requests for deleting existing blog posts.
    """

    template_name = "Tech/delete_blog_post.html"

    def get(self, request, blog_post_id):
        blog_post = get_object_or_404(BlogPost, id=blog_post_id, author=request.user)

        return render(request, self.template_name, {"blog_post": blog_post})

    def post(self, request, blog_post_id):
        blog_post = get_object_or_404(BlogPost, id=blog_post_id, author=request.user)
        blog_post.delete()

        return redirect("dashboard")


class BlogPostsView(View):
    """
    Displays a list of all blog posts.

    Attributes:
        template_name (str): The HTML template used for rendering the blog post list.
        per_page (int): Number of blog posts to display per page.

    Methods:
        get(request): Handles GET requests for displaying the list of all blog posts.
    """

    template_name = "Tech/blog_post_list.html"
    per_page = 10

    def get(self, request):

        all_blog_posts = BlogPost.objects.all().order_by("-pub_date")
        blog_post_count = all_blog_posts.count()
        paginator = Paginator(all_blog_posts, self.per_page)
        page = request.GET.get("page")

        try:
            blog_posts = paginator.page(page)
        except PageNotAnInteger:
            blog_posts = paginator.page(1)
        except EmptyPage:
            blog_posts = paginator.page(paginator.num_pages)

        return render(
            request,
            self.template_name,
            {"blog_posts": blog_posts, "blog_post_count": blog_post_count},
        )


class BlogPostDetailView(View):
    """
    Displays a detailed view of a single blog post.

    Attributes:
        template_name (str): The HTML template used for rendering the blog post detail.

    Methods:
        get(request, post_slug): Handles GET requests for displaying a detailed view of a single blog post.
    """

    template_name = "Tech/blog_post_detail.html"

    def get(self, request, post_slug):
        current_post = get_object_or_404(BlogPost, slug=post_slug)
        previous_post = (
            BlogPost.objects.filter(pub_date__lt=current_post.pub_date)
            .order_by("-pub_date")
            .first()
        )
        next_post = (
            BlogPost.objects.filter(pub_date__gt=current_post.pub_date)
            .order_by("pub_date")
            .first()
        )

        context = {
            "current_post": current_post,
            "previous_post": previous_post,
            "next_post": next_post,
        }

        return render(request, self.template_name, context)


class AuthorPostView(View):
    """
    Displays a list of blog posts authored by a specific author.

    Attributes:
        template_name (str): The HTML template used for rendering the author's posts.

    Methods:
        get(request, author_name): Handles GET requests for displaying the author's posts.
    """

    template_name = "Tech/author_posts.html"

    def get(self, request, author_name):
        # Split the author_name into first name and last name
        first_name, last_name = author_name.split()

        # Query the CustomUser model to get the author's profile
        author = CustomUser.objects.filter(
            Q(first_name=first_name) & Q(last_name=last_name)
        ).first()

        # Filter blog posts by author's first name or last name
        blog_posts = BlogPost.objects.filter(
            Q(author__first_name=first_name) | Q(author__last_name=last_name)
        )

        # Count the Author Blog Post
        blog_post_count = blog_posts.count()

        # Number of posts to display per page
        posts_per_page = 10

        # Create a Paginator object
        paginator = Paginator(blog_posts, posts_per_page)

        # Get the current page number from the request's GET parameters
        page = request.GET.get("page")

        try:
            # Get the Page object for the requested page
            blog_posts = paginator.page(page)
        except PageNotAnInteger:
            # If the page is not an integer, display the first page
            blog_posts = paginator.page(1)
        except EmptyPage:
            # If the page is out of range, display the last page
            blog_posts = paginator.page(paginator.num_pages)

        context = {
            "author": author,
            "blog_posts": blog_posts,
            "blog_post_count": blog_post_count,
        }

        return render(request, self.template_name, context)


class CategoryView(View):
    """
    Displays a list of blog posts for a specific category.

    Attributes:
        template_name (str): The HTML template used for rendering the author's posts.

    Methods:
        get(request, category): Handles GET requests for displaying category-specific blog posts.
    """

    template_name = "Tech/category_posts.html"

    def get(self, request, category):

        blog_posts = BlogPost.objects.filter(
            categories__iexact=category, status="published"
        ).order_by("-pub_date")

        blog_post_count = blog_posts.count()
        per_page = 10

        paginator = Paginator(blog_posts, per_page)

        page = request.GET.get("page")

        try:
            blog_posts = paginator.page(page)

        except PageNotAnInteger:
            blog_posts = paginator.page(1)

        except EmptyPage:
            blog_posts = paginator.page(paginator.num_pages)

        context = {
            "blog_posts": blog_posts,
            "category": category,
            "blog_post_count": blog_post_count,
        }

        return render(request, self.template_name, context)


class CustomPasswordChangeView(LoginRequiredMixin, View):
    """
    Handles user password change functionality.

    Attributes:
        template_name (str): The HTML template used for rendering the password change page.

    Methods:
        get(request, *args, **kwargs): Handles GET requests for displaying the password change page.
        post(request, *args, **kwargs): Handles POST requests for changing the user's password.
    """

    template_name = "Tech/password_change.html"

    def get(self, request, *args, **kwargs):

        form = PasswordChangeForm(request.user)
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect("password_change")
        else:
            if "old_password" in form.errors:
                messages.error(request, "Old password is incorrect.")
            if "new_password2" in form.errors:
                messages.error(
                    request, "Passwords do not match. Enter the correct password."
                )

        return render(request, self.template_name, {"form": form})


class CustomPasswordResetView(LoginRequiredMixin, View):
    """
    Handles user password reset functionality.

    Attributes:
        template_name (str): The HTML template used for rendering the password reset page.

    Methods:
        get(request): Handles GET requests for displaying the password reset page.
        post(request): Handles POST requests for initiating the password reset process.
    """

    template_name = "Tech/password_reset.html"

    def get(self, request):

        form = PasswordResetForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):

        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Process the password reset logic here
            messages.error(
                request,
                "Password reset isn't working. Please contact at help@bloggersunity.com.",
            )
            return redirect("password_reset")
        else:
            messages.error(
                request,
                "Password reset isn't working. Please contact at help@bloggersunity.com.",
            )
            form = PasswordResetForm()  # Reset the form
            context = {
                "form": form,
            }
            return render(
                request, self.template_name, context
            )  # You can customize this response
