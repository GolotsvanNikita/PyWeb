from django import forms

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
        min_length=13,
        max_length=13,
        label="Phone number",
        error_messages=
        {
            'required': 'Phone number input required',
            'min_length': 'Phone number must have 9 digits (without phone code)',
            'max_length': "Phone number must have 9 digits (without phone code)"
        }
    ))