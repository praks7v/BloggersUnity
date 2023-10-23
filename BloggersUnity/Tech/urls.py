from django.urls import path

from . import views
from .views import CustomLoginView, CustomLogoutView, CustomPasswordChangeView, CustomPasswordResetView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

    # User related Urls
    path('signup/', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user/profile/', views.user_profile, name='user_profile'),

    # Blog Post related Urls
    path('user/blog/posts/', views.user_blog_posts, name='user_blog_posts'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('blog/<int:blog_post_id>/edit', views.edit_blog_post, name='edit_blog_post'),
    path('blog/<int:blog_post_id>/delete', views.delete_blog_post, name='delete_blog_post'),
    path('blog/', views.BlogPostListView.as_view(), name='blog_post_lists'),
    path('blog/<slug:post_slug>/', views.blog_post_detail, name='blog_post_detail'),

    # password related urls
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset')
]
