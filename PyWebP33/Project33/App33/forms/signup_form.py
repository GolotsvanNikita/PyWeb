from django import forms
from django.core.exceptions import ValidationError
from datetime import date
import re


class SignupForm(forms.Form):
    first_name = forms.CharField(
        min_length=2,
        max_length=64,
        label="Name",
        error_messages={
            'required': 'Name input required',
            'min_length': 'Name must have no less 2 symbols',
            'max_length': "Name don`t must be upper 64 symbols"
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=64,
        label="Surname",
        error_messages={
            'required': 'Surname input required',
            'min_length': 'Surname must have no less 2 symbols',
            'max_length': "Surname don`t must be upper 64 symbols"
        }
    )
    phone_num = forms.CharField(
        min_length=10,
        max_length=13,
        label="Phone number",
        error_messages={
            'required': 'Phone number input required',
            'min_length': 'Phone number must no less 10 digits',
            'max_length': "Phone number must not be upper 13 digits"
        }
    )
    email = forms.CharField(
        min_length=6,
        max_length=128,
        label="E-mail",
        error_messages={
            'required': 'E-mail number input required',
            'min_length': 'E-mail must no less 6 digits',
            'max_length': "E-mail number must have 128 digits"
        }
    )
    birthdate = forms.DateField(
        required=False,
        label="Birthdate",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    login = forms.CharField(
        min_length=3,
        max_length=32,
        label="Login",
        error_messages={
            'required': 'Login number input required',
            'min_length': 'Login must no less 6 digits',
            'max_length': "Login number must have 32 digits"
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password input required'
        }
    )
    repeat = forms.CharField(
        widget=forms.PasswordInput(),
        label="Repeat"
    )

    def clean(self):
        cleaned_data = super().clean()

        if 'password' in cleaned_data:
            password = cleaned_data['password']
            if len(password) < 4:
                self.add_error('password', ValidationError('Password must have no less 4 symbols'))
            if not re.search(r'\d', password):
                self.add_error('password', ValidationError('Password must have at least one digit'))
            if not re.search(r'\W', password):
                self.add_error('password', ValidationError('Password must have at least one special symbol'))

        if 'repeat' in cleaned_data and 'password' in cleaned_data:
            repeat = cleaned_data['repeat']
            if repeat != cleaned_data.get('password'):
                self.add_error('repeat', ValidationError('Passwords are not equal'))

        if 'first_name' in cleaned_data:
            first_name = cleaned_data['first_name']
            if re.search(r'\d', first_name):
                self.add_error('first_name', ValidationError('Digits are not allowed in name'))

        if 'phone_num' in cleaned_data:
            phone_num = cleaned_data['phone_num']
            if not re.match(r'^0\d+$', phone_num):
                self.add_error('phone_num', ValidationError('Phone number must start with 0 and contain only digits'))

        if 'email' in cleaned_data:
            email = cleaned_data['email']
            if '@' not in email or '.' not in email:
                self.add_error('email', ValidationError('Invalid email format'))

        if 'login' in cleaned_data:
            login = cleaned_data['login']
            if ':' in login:
                self.add_error('login', ValidationError('Login cannot contain the ":" symbol'))

        if 'birthdate' in cleaned_data:
            b_date = cleaned_data['birthdate']
            if b_date:
                today = date.today()

                if b_date > today:
                    self.add_error('birthdate', ValidationError('Birthdate cannot be in the future'))

                else:
                    age = today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))
                    if age < 18:
                        self.add_error('birthdate', ValidationError('You must be at least 18 years old to register'))

        return cleaned_data