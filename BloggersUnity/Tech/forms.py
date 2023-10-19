from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, BlogPost


class CustomSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    email = forms.EmailField(max_length=254, help_text="Required. Enter your email address.")

    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_picture'].required = False


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'status', 'image']


class BlogPostEditForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'status', 'image']
