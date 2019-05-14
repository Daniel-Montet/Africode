from django import forms
from django.core import validators

def must_be_empty(value):
    """  This is a custom validator """
    if value:
        raise forms.ValidationError('is not empty')

class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget= forms.HiddenInput, label="Leave Empty", validators=[must_be_empty])

    # def clean_honeypot(self):#not reusable
    #     """ Clean field validator"""
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError("Honeypot should be left empty. Bad bot!")
    #     return honeypot

    def clean(self):
        """ Performs integrity check for the whole form and its fields """
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError("You need to enter the same email in both fields")