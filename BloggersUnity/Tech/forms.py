from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import ContactMessage
from .models import CustomUser, BlogPost


class CustomSignUpForm(UserCreationForm):
    """
    Custom Sign-Up Form for user registration.

    This form extends the built-in UserCreationForm with an additional 'email' field.
    It provides validation and custom error messages for email and password fields.
    """

    email = forms.EmailField(max_length=254, help_text="Required. Enter your email address.",
                             error_messages={
                                 'invalid': "Please enter a valid email address.",
                                 'unique': "This email address is already in use. Please choose a different one."
                             })

    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ('username', 'email', 'password1', 'password2')

    error_messages = {
        'username': {
            'unique': "This username is already in use. Please choose a different one."
        },
        # Define a custom error message for the 'password_mismatch' case
        'password1': {
            'password_mismatch': "The password fields didn't match."
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages[
            'unique'] = "This username is already in use. Please choose a different one."

    def clean_password2(self):
        # Custom validation to ensure password fields match.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password1']['password_mismatch'],
                code='password_mismatch',
            )

        return password2


class UserProfileForm(forms.ModelForm):
    """
    User Profile Form for updating user profile details.
    """

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'bio', 'profile_picture', 'date_of_birth']

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')

        if profile_picture:
            # Limit profile picture size to 5MB
            if profile_picture.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise ValidationError("Profile picture size should not exceed 5MB.")

        return profile_picture

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_picture'].required = False


class BlogPostForm(forms.ModelForm):
    """
    Form for creating new blog posts.
    """

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'status', 'image', 'categories', 'status']


class BlogPostEditForm(forms.ModelForm):
    """
    Form for editing existing blog posts.
    """

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'status', 'image', 'categories', 'status']


class ContactForm(forms.ModelForm):
    """
    Contact Form for submitting messages.
    """

    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
