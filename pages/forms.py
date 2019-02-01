from django import forms

from .models import Page

class EmailForm(forms.Form):

 email = forms.EmailField(required = True)
 	

class PageForm(forms.ModelForm):
	class Meta:
 		model = Page
 		fields = '__all__'

