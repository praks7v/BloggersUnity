from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, BlogPost


class CustomSignUpForm(UserCreationForm):
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
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password1']['password_mismatch'],
                code='password_mismatch',
            )

        return password2


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'bio', 'profile_picture', 'date_of_birth']

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
