from django import forms
from .models import Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

######

# class ContactForm(forms.Form):
#     email = forms.EmailField(required=True, label='Enter your email')
#     subject = forms.CharField(required=True, label='Type the subject')
#     message = forms.CharField(widget=forms.Textarea, required=True, label='Type the Message')
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=200, label='Enter your username')
#     password = forms.CharField(max_length=200, label='Enter your password')
#
#
# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


class BookForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title, Author', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Script', required=True, widget=forms.Textarea(attrs={"class": "form-control", "row":5,}))
    is_published=forms.BooleanField(label='Published')
    category = forms.ModelChoiceField(empty_label='Choose Category', label='Category', queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))

