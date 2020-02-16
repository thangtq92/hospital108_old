from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('full_name', 'address', 'dob', 'gender', 'about','phone_number ')