from django import forms
from validate_email import validate_email
class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False,label='Podaj email')
    message = forms.CharField(widget=forms.Textarea)

def clean_email(self):
    em = self.cleaned_data['email']
    if not validate_email(em):
        raise forms.ValidationError('Niepoprawny email!')
    return em

class ContactFormStudent(forms.Form):
	imie = forms.CharField(max_length=20)
	nazwisko = forms.CharField(max_length=20)
	przedmiot = forms.CharField(max_length=30)
		