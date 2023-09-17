import attrs
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms.utils import ErrorList

class BootstrapErrorList(ErrorList):
    def __init__(self, initlist=None, error_class=None, renderer=None):
        error_class = "alert alert-warning "
        super().__init__(initlist=initlist, error_class=error_class, renderer=renderer)

class BaseForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = BootstrapErrorList
class CustomUserCreationForm(BaseUserCreationForm, BaseForm):
    is_authenticated = True
    password1 = forms.CharField(label="", widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "id": "registerPassword",
        "name": "password1",
        "type":"password",
        "placeholder": "Password",
        "required": True}))
    password2 = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "id": "confirmPassword",
        "name": "password2",
        "placeholder": "Confirm Password",
        "required": True}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control mb-3", "required": True, "placeholder": "Username"})
        self.fields["email"].widget.attrs.update({"class": "form-control mb-3", "required": True,"placeholder": "Email"})
        self.fields["first_name"].widget.attrs.update({"class": "form-control mb-3", "required": True, "placeholder": "First Name"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control mb-3", "required": True, "placeholder": "Last Name"})
        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["first_name"].label = ""
        self.fields["last_name"].label = ""
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm, BaseForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "id": "registerUsername",
        "name": "username",
        "placeholder": "Username",
        "required": True}))
    password = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "id": "registerPassword",
        "name": "password",
        "placeholder": "Password",
        "type": "password",
        "required": True}))
    class Meta:
        model = User

