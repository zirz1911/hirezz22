from django import forms

from members.models import *
from django.contrib.auth.forms import UserCreationForm
from .models import myUser
from django.contrib.auth.models import User

# ทำให้ใช้ custom user model ได้
from django.contrib.auth import get_user_model

User = get_user_model()


# Admin form
class PostFormCreateAdmin(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'myUser', 'topic', 'price', 'description', 'contactFb', 'contactTw', 'contactEmail', 'contactOther',
            'image',
            'image2', 'image3')
        widgets = {
            'myUser': forms.Select(attrs={'class': 'form-control'}),
            'topic': forms.TextInput({'class': 'form-control', 'required': 'required', 'maxlength': '200'}),
            'price': forms.TextInput({'class': 'form-control', 'required': 'required', 'Min': '1'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
            'contactFb': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://www.facebook.com/test111'}),
            'contactTw': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://twitter.com/Test111'}),
            'contactEmail': forms.TextInput(
                {'class': 'form-control', 'required': 'required', 'placeholder': 'Example: example@email.com'}),
            'contactOther': forms.TextInput({'class': 'form-control', 'required': 'required',
                                             'placeholder': 'Example: https://twitter.com/Test111'}),

        }


# User form
class PostFormCreate(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'topic', 'price', 'description', 'contactFb', 'contactTw', 'contactEmail', 'contactOther', 'image',
            'image2',
            'image3')
        widgets = {

            'topic': forms.TextInput({'class': 'form-control', 'required': 'required', 'maxlength': '200'}),
            'price': forms.TextInput({'class': 'form-control', 'required': 'required', 'Min': '1'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
            'contactFb': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://www.facebook.com/test111'}),
            'contactTw': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://twitter.com/Test111'}),
            'contactEmail': forms.TextInput(
                {'class': 'form-control', 'required': 'required', 'placeholder': 'Example: example@email.com'}),
            'contactOther': forms.TextInput({'class': 'form-control', 'required': 'required',
                                             'placeholder': 'Example: https://twitter.com/Test111'}),

        }


# Update Admin
class PostFormUpdateAdmin(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('myUser', 'topic', 'price', 'description', 'contactFb', 'contactTw', 'contactEmail', 'contactOther')
        widgets = {
            'myUser': forms.Select(attrs={'class': 'form-control'}),
            'topic': forms.TextInput({'class': 'form-control', 'required': 'required', 'maxlength': '200'}),
            'price': forms.TextInput({'class': 'form-control', 'required': 'required', 'Min': '1'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
            'contactFb': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://www.facebook.com/test111'}),
            'contactTw': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://twitter.com/Test111'}),
            'contactEmail': forms.TextInput(
                {'class': 'form-control', 'required': 'required', 'placeholder': 'Example: example@email.com'}),
            'contactOther': forms.TextInput({'class': 'form-control', 'required': 'required',
                                             'placeholder': 'Example: https://twitter.com/Test111'}),

        }


# User Update Form
class PostFormUpdate(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('topic', 'price', 'description', 'contactFb', 'contactTw', 'contactEmail', 'contactOther')
        widgets = {
            'topic': forms.TextInput({'class': 'form-control', 'required': 'required', 'maxlength': '200'}),
            'price': forms.TextInput({'class': 'form-control', 'required': 'required', 'Min': '1'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
            'contactFb': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://www.facebook.com/test111'}),
            'contactTw': forms.TextInput({'class': 'form-control', 'required': 'required',
                                          'placeholder': 'Example: https://twitter.com/Test111'}),
            'contactEmail': forms.TextInput(
                {'class': 'form-control', 'required': 'required', 'placeholder': 'Example: example@email.com'}),
            'contactOther': forms.TextInput({'class': 'form-control', 'required': 'required',
                                             'placeholder': 'Example: https://twitter.com/Test111'}),

        }


class PostPicFormUpdate(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('image', 'image2', 'image3')
        widgets = {
        }


# ------------------------------------------------------------------------ Freelancer ---------------------------------------------------------
# Add Freelance User
class FreelancerCreateProfile(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ('gender', 'good_at', 'style', 'description', 'profile')
        GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
        widgets = {
            'gender': forms.RadioSelect(choices=GENDER_CHOICES, ),
            'good_at': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Illustrator, Photoshop, etc...'}),
            'style': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Chibi, Nature, Cyber Punk, etc...'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
        }


# Add Freelance Admin
class FreelancerCreateProfileAdmin(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ('myUser', 'gender', 'good_at', 'style', 'description', 'profile')
        GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
        widgets = {
            'myUser': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=GENDER_CHOICES),
            'good_at': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Illustrator, Photoshop, etc...'}),
            'style': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Chibi, Nature, Cyber Punk, etc...'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
        }


# Update Freelancer Admin
class FreelancerUpdateAdmin(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ('myUser', 'gender', 'good_at', 'style', 'description')
        GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
        widgets = {
            'myUser': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=GENDER_CHOICES),
            'good_at': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Illustrator, Photoshop, etc...'}),
            'style': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Chibi, Nature, Cyber Punk, etc...'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
        }


# User Update Freelancer
class FreelancerUpdate(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ('gender', 'good_at', 'style', 'description')
        GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
        widgets = {
            'gender': forms.RadioSelect(choices=GENDER_CHOICES, ),
            'good_at': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Illustrator, Photoshop, etc...'}),
            'style': forms.TextInput({'class': 'form-control', 'required': 'required', 'placeholder': 'Example: Chibi, Nature, Cyber Punk, etc...'}),
            'description': forms.Textarea({'class': 'form-control', 'required': 'required', 'row': 5, 'cols': 60}),
        }


class ProfileFreelancerFormUpdate(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ('profile',)
        widgets = {
        }


#Register User Form
class RegisterUserForm(UserCreationForm):
    user_email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control'}))
    user_name = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    user_lastname = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    user_job = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'user_id', 'user_name', 'user_lastname', 'user_email', 'user_job', 'password1', 'password2', 'user_profile')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

