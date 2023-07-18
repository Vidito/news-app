from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].required = True
        self.fields['email'].required = True
    # email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username', 'email', 'age',
        )


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'age',
        )
