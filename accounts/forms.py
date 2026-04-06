from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    password = None  # No queremos editar la password acá
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']