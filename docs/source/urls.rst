Urls
====

.. automodule:: Tech.urls
   :members:

.. automodule:: BloggersUnity.urls
   :members:


Project's Urls
--------------
#. Imports for project's urls

.. code-block:: python
   :linenos:

   from django.conf import settings
   from django.conf.urls.static import static
   from django.contrib import admin
   from django.urls import path, include

#. Urlpatterns of Project's Urls

.. code-block:: python
   :linenos:

   urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('Tech.urls')),
   ]

#. Serve media files during development

.. code-block:: python
   :linenos:

   if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Tech apps Urls
---------------
Imports
------------

.. code-block:: python
   :linenos:

   from django.urls import path
   from . import views
   from .views import CustomPasswordChangeView, CustomPasswordResetView

Main pages Urls
---------------

- `/`: Home page.
- `/about/`: About page.
- `/contact/`: Contact page.
- `/faqs/`: Frequently Asked Questions page.
- `/privacy_policy/`: Privacy Policy page.

.. code-block:: python
   :linenos:

   path('', views.HomeView.as_view(), name='home'),
   path('about/', views.AboutView.as_view(), name='about'),
   path('contact/', views.ContactView.as_view(), name='contact'),
   path('faqs/', views.FaqsView.as_view(), name='faqs'),
   path('privacy_policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),

User-Related URLs
-----------------

- `/signup/`: User registration.
- `/login/`: User login.
- `/logout/`: User logout.
- `/user/profile/`: User profile.

.. code-block:: python
   :linenos:

   path('signup/', views.SignupView.as_view(), name='signup'),
   path('login/', views.CustomLoginView.as_view(), name='login'),
   path('logout/', views.CustomLogoutView.as_view(), name='logout'),
   path('user/profile/', views.UserProfileView.as_view(), name='user_profile'),

User Blog Post URLs
-------------------

- `/dashboard/`: User's blog post dashboard.
- `/create/`: Create a new blog post.
- `/blog/<int:blog_post_id>/edit/`: Edit a specific blog post.
- `/blog/<int:blog_post_id>/delete/`: Delete a specific blog post.

.. code-block:: python
   :linenos:

   path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
   path('create/', views.CreateBlogPostView.as_view(), name='create_blog_post'),
   path('blog/<int:blog_post_id>/edit', views.EditBlogPostView.as_view(), name='edit_blog_post'),
   path('blog/<int:blog_post_id>/delete', views.DeleteBlogPostView.as_view(), name='delete_blog_post'),

Blog Post URLs
--------------

- `/blog/`: List of all blog posts.
- `/blog/<slug:post_slug>/`: Detailed view of a specific blog post.
- `/author-posts/<str:author_name>/`: Blog posts by a specific author.

.. code-block:: python
   :linenos:

   path('blog/', views.BlogPostsView.as_view(), name='blog_post_lists'),
   path('blog/<slug:post_slug>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
   path('author-posts/<str:author_name>/', views.AuthorPostView.as_view(), name='author_posts'),

Category URLs
-------------

- `/category/`: List of all categories.
- `/category/<str:category>/`: Blog posts in a specific category.

.. code-block:: python
   :linenos:

   path('category/', views.CategoryView.as_view(), name='all_categories'),
   path('category/<str:category>/', views.CategoryView.as_view(), name='category_posts'),

Password-Related URLs
---------------------

- `/password_change/`: Change password.
- `/password_reset/`: Reset password.

.. code-block:: python
   :linenos:

   path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
   path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset')

