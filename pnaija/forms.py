from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Firstname'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Lastname'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    location = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Location'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    meterid = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'MeterId'}))
    office = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'office'}))

    def clean_password(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password')
        print(password)
        print(password1)
        if password1 != password:
            raise forms.ValidationError('Password must match!')
        return data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken ')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not "gmail.com" in email:
            raise forms.ValidationError('Email has to be gmail.com')
        else:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError('Email is taken')
        return email
