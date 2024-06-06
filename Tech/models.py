from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class CustomUserManager(BaseUserManager):
    # Custom user manager for the CustomUser model.

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a standard user with the given username, email, and password.

        Args:
            username (str): The username for the user.
            email (str): The email address for the user.
            password (str): The user's password.
            extra_fields (dict): Extra fields to include in the user's data.

        Returns:
            CustomUser: The created user.
        """

        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given username, email, and password.

        Args:
            username (str): The username for the superuser.
            email (str): The email address for the superuser.
            password (str): The superuser's password.
            extra_fields (): Extra fields to include in the superuser's data.

        Returns:
            CustomUser: The created superuser.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Custom user model for your application.

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        """
        Return a string representation of the user.

        Returns:
            str: The user's full name if available, or the username or email.
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.username:
            return self.username
        else:
            return self.email


class BlogPost(models.Model):
    # Model for blog posts.

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    CATEGORY_CHOICES = (
        ("Aerospace", "Aerospace"),
        ("Artificial_Intelligence", "Artificial Intelligence"),
        ("Automotive", "Automotive"),
        ("Biotechnology", "Biotechnology"),
        ("Cybersecurity", "Cybersecurity"),
        ("Fintech", "Fintech"),
        ("Gaming", "Gaming"),
        ("IoT", "Internet of Things"),
        ("Robotics", "Robotics"),
        ("Other", "Other"),
    )

    categories = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, default="Other"
    )

    slug = models.SlugField(unique=True, max_length=255, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        """
        Save the blog post, generate a unique slug, and handle duplicates.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """

        # Generate the slug based on the  title
        self.slug = slugify(self.title)

        # Check if the new slug is unique
        counter = 1
        new_slug = self.slug
        while BlogPost.objects.filter(slug=new_slug).exclude(pk=self.pk).exists():
            new_slug = f"{self.slug}-{counter}"
            counter += 1
        self.slug = new_slug

        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the blog post.

        Returns:
            str: The title of the blog post.
        """
        return self.title


class ContactMessage(models.Model):
    # Model for contact messages.

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
