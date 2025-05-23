from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='وارد کردن ایمیل معتبر الزامی است.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'نظر خود را بنویسید...'
            }),
        }