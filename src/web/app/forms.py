from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models.property_models import Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label="Company Name")
    financial_id_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["financial_id_number", "email",
                  "username", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['build_status', 'is_active', 'start_month', 'construction_type',
                  'date_diff', 'description', 'date_in', 'property_type', 'end_week',
                  'typology_type', 'id', 'coordinates', 'boundary_id', 'id_uda', 'title',
                  'listing_type', 'date']
