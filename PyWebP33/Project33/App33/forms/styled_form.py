from django import forms
from django.core.exceptions import ValidationError
import re

class StyledForm(forms.Form):
    first_name = (forms.CharField
    (
        min_length=2,
        max_length=6,
        label="Name",
        error_messages=
        {
            'required': 'Name input required',
            'min_length': 'Name must have no less 2 symbols',
            'max_length': "Name don`t must be upper 64 symbols"
        }
    ))
    last_name = (forms.CharField
    (
        min_length=2,
        max_length=6,
        label="Surname",
        error_messages=
        {
            'required': 'Surname input required',
            'min_length': 'Surname must have no less 2 symbols',
            'max_length': "Surname don`t must be upper 64 symbols"
        }
    ))
    phone_num = (forms.CharField
    (
        min_length=10,
        max_length=10,
        label="Phone number",
        error_messages=
        {
            'required': 'Phone number input required',
            'min_length': 'Phone number must have 10 digits',
            'max_length': "Phone number must have 10 digits"
        }
    ))
    password = (forms.CharField
    (
        widget=forms.PasswordInput(),
        error_messages =
        {
            'required': 'Password input required'            
        }
    ))

    repeat = (forms.CharField
    (
        widget=forms.PasswordInput(),
        required=False
    ))

    is_agree = (forms.BooleanField
    (
        help_text='I accept privacy policy',
        error_messages =
        {
            'required': 'You must accept with privacy policy site'
        }
    ))

    def clean(self):
        cleaned_data = super().clean()
        if 'password' in cleaned_data:
            password = cleaned_data['password']
            if len(password) < 4:
                self.add_error(
                    'password',
                    ValidationError('Password must have no less 4 symbols')
                )
            if not re.search(r'\d', password):
                self.add_error(
                    'password',
                    ValidationError('Password must have such a one digit')
                )
            if not re.search(r'\W', password):
                self.add_error(
                    'password',
                    ValidationError('Password must have such a one special symbol')
                )

        if 'repeat' in cleaned_data:
            repeat = cleaned_data['repeat']
            if repeat != cleaned_data.get('password', ''):
                self.add_error(
                    'repeat',
                    ValidationError('Passwords are not equal')
                )

        if 'first_name' in cleaned_data:
            first_name = cleaned_data['first_name']
            if re.search(r'\d', first_name):
                self.add_error(
                    'first_name',
                    ValidationError('In name not allowed digits')
                )

        if 'phone_num' in cleaned_data:
            phone_num = cleaned_data['phone_num']
            if not re.search(r'^0\d', phone_num):
                self.add_error(
                    'phone_num',
                    ValidationError('Phone number must be start at digit 0 and have only digits')
                )
        return cleaned_data
            