from importlib.metadata import files
from django import forms
from web.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

        