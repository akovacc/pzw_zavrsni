from django import forms
from main.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','surname','email','phone_number']