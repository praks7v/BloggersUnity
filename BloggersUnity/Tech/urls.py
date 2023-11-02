from django.urls import path

from . import views
from .views import CustomPasswordChangeView, CustomPasswordResetView

# Urls of Tech app's
urlpatterns = [

    # Main pages Urls
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faqs/', views.FaqsView.as_view(), name='faqs'),
    path('privacy_policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),

    # User related Urls
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('user/profile/', views.UserProfileView.as_view(), name='user_profile'),

    # User Blog Post Urls
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create/', views.CreateBlogPostView.as_view(), name='create_blog_post'),
    path('blog/<int:blog_post_id>/edit', views.EditBlogPostView.as_view(), name='edit_blog_post'),
    path('blog/<int:blog_post_id>/delete', views.DeleteBlogPostView.as_view(), name='delete_blog_post'),

    # Blog Post related Urls
    path('blog/', views.BlogPostsView.as_view(), name='blog_post_lists'),
    path('blog/<slug:post_slug>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('author-posts/<str:author_name>/', views.AuthorPostView.as_view(), name='author_posts'),

    # Urls for Categories
    path('category/', views.CategoryView.as_view(), name='all_categories'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category_posts'),

    # Password related urls
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset')
]
