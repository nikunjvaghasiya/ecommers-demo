from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=55, label="Your name")
    email = forms.EmailField(max_length=55, label="Your email")
    password = forms.PasswordInput()

    