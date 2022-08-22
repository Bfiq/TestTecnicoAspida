from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formRegister(UserCreationForm):

	username = forms.CharField(label='identificación')
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
	first_name = forms.CharField(label='Nombres')
	last_name = forms.CharField(label='Apellidos')

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username','password1', 'password2']
		help_texts = {k:"" for k in fields }