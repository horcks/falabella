from django import forms
from django.db.models import Q
from apps.users.models import *
from allauth.account.adapter import get_adapter
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
	new_password=forms.CharField(widget=forms.PasswordInput())
	# repeat_password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = [
		'first_name',
		'last_name',
		'email',
		'new_password',
		# 'repeat_password',
		'username'
		]
	def clean_first_name(self):
		first_name = self.cleaned_data.get("first_name")
		if not first_name:
			raise forms.ValidationError("Este campo es requerido")
		return first_name

	def clean_last_name(self):
		last_name = self.cleaned_data.get("last_name")
		if not last_name:
			raise forms.ValidationError("Este campo es requerido")
		return last_name
		
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not email:
			raise forms.ValidationError("Este campo es requerido")
		return email

	# def clean_new_password(self):
	# 	print(self.cleaned_data.get('new_password'))
	# 	print(self.cleaned_data.get('repeat_password'))
	# 	new_password=self.cleaned_data.get('new_password')
	# 	repeat_password=self.cleaned_data.get('repeat_password')
	# 	if new_password!=repeat_password:
	# 		raise forms.ValidationError(('Las contraseñas deben ser iguales'), code='invalid')
	# 	else:
	# 		validation=get_adapter().clean_password(new_password)
	# 	return self.cleaned_data	
		
	def clean_email(self):
		email = self.cleaned_data['email']
		validation=User.objects.filter(Q(email=email)|Q(username=email)).exclude(pk=self.instance.pk).exists()
		if validation:
			raise forms.ValidationError(('Email existente, favor ingrese un dato valido.'), code='invalid')
		return email

class ExtendUserForm(forms.ModelForm):
	class Meta:
		model = Extended_User
		fields = [
			'document_number',
			'phone1',
			'phone2',
			'address',
			#'photo',
			'document_type',
			'date_birth',
			'description_address',
		]