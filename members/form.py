from django import forms
from members.models import *
from django.contrib.auth.forms import UserCreationForm
from .models import myUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class PostFormCreate(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('topic', 'price', 'description', 'contactFb', 'contactTw', 'contactEmail', 'contactOther', 'image', 'image2', 'image3')
        widgets = {
            'topic': forms.TextInput({'class': 'form-control', 'required': 'required', 'maxlength': '200'}),
            'price': forms.TextInput({'class': 'form-control', 'required': 'required', 'Min': '1'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
            'contactFb': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'contactTw': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: https://twitter.com/Test111'}),
            'contactEmail': forms.TextInput({'class': 'form-control', 'required': 'required'}),
            'contactOther': forms.TextInput({'class': 'form-control', 'required': 'required'}),


        }


class RegisterUserForm(UserCreationForm):
    user_email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control'}))
    user_name = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    user_lastname = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    user_job = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'user_lastname', 'user_email', 'user_job', 'password1', 'password2', 'user_profile')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

