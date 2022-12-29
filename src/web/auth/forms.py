from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label="Company Name")
    financial_id_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["financial_id_number", "email",
                  "username", "password1", "password2"]
