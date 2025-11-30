from django import forms
from django.core.exceptions import ValidationError
import re
from datetime import datetime, date, timedelta


class DeliveryForm(forms.Form):
    first_name = forms.CharField(
        min_length=2,
        max_length=64,
        label="Name",
        error_messages={
            'required': "Name input required",
            'min_length': "Name must be no less 2 digits",
            'max_length': "Name must not be upper 64 digits"
        })

    last_name = forms.CharField(
        min_length=2,
        max_length=64,
        label="Last",
        error_messages={
            'required': "Last name input required",
            'min_length': "Last name must be no less 2 digits",
            'max_length': "Last name must not be upper 64 digits"
        })

    Street_Address = forms.CharField(
        min_length=10,
        max_length=50,
        label="Street Address",
        error_messages={
            'required': "Street address input required",
            'min_length': "Street address must be no less 10 letters",
            'max_length': "Street address must not be upper 50 letters"
        })

    Street_Address_L2 = forms.CharField(
        min_length=5,
        max_length=50,
        label="Street Address Line 2",
        error_messages={
            'required': "Street address line 2 input required",
            'min_length': "Street address line 2 must be no less 5 letters",
            'max_length': "Street address line 2 must not be upper 50 letters"
        })

    City = forms.CharField(
        min_length=2,
        max_length=25,
        label="City",
        error_messages={
            'required': "City input required",
            'min_length': "City must be no less 2 letters",
            'max_length': "City must not be upper 25 letters"
        })

    Region = forms.CharField(
        min_length=8,
        max_length=15,
        label="Region",
        error_messages={
            'required': "Region input required",
            'min_length': "Region must be no less 8 letters",
            'max_length': "Region must not be upper 15 letters"
        })

    index = forms.CharField(
        min_length=4,
        max_length=8,
        label="Postal / Zip Code",
        error_messages={
            'required': "Postal / Zip Code input required",
            'min_length': "Postal / Zip Code must be no less 4 digits",
            'max_length': "Postal / Zip Code must not be upper 8 digits"
        })

    STATUS_CHOICES = [
        ('uk', 'Ukraine')
    ]
    list = forms.ChoiceField(choices=STATUS_CHOICES, initial='uk')

    Date = forms.DateField(
        label="Date",
        widget=forms.DateInput(attrs={'type': 'date'}),
        error_messages={'required': "Date input required"}
    )

    Time = forms.TimeField(
        label="Time",
        widget=forms.TimeInput(attrs={'type': 'time'}),
        error_messages={'required': "Time input required"}
    )

    is_agree = forms.BooleanField(
        help_text="I accept privacy policy",
        error_messages={
            'required': "You must accept privacy policy"
        }
    )

    def clean(self):
        cleaned_data = super().clean()

        if 'index' in cleaned_data:
            index = cleaned_data['index']
            if re.search(r"\D", index):
                self.add_error("index", ValidationError("index must have only digits"))

        if 'Date' in cleaned_data:
            input_date = cleaned_data['Date']
            if input_date <= date.today():
                self.add_error("Date", ValidationError("Date must be in the future (min 1 day different)"))

        if 'Time' in cleaned_data:
            input_time = cleaned_data['Time']
            start_time = datetime.strptime("09:00", "%H:%M").time()
            end_time = datetime.strptime("18:00", "%H:%M").time()

            if not (start_time <= input_time <= end_time):
                self.add_error("Time", ValidationError("Work time is at 9:00 to 18:00"))


        if 'City' in cleaned_data:
            City = cleaned_data['City']
            if not City[0].isupper():
                self.add_error("City", ValidationError("City must start at upper letter"))

        if 'Street_Address' in cleaned_data:
            Street_Address = cleaned_data['Street_Address']
            if not Street_Address[0].isupper():
                self.add_error("Street_Address", ValidationError("Street address must start at upper letter"))

        if 'Street_Address_L2' in cleaned_data:
            Street_Address_L2 = cleaned_data['Street_Address_L2']
            if not Street_Address_L2[0].isupper():
                self.add_error("Street_Address_L2", ValidationError("Street address line 2 must start at upper letter"))

        return cleaned_data