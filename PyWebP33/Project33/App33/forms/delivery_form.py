from django import forms
from django.core.exceptions import ValidationError
import re   # regular expressions

# класи-форми описують склад форм у вигляді спеціальних елементів
class DeliveryForm(forms.Form) :
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
            'required': "Необхідно ввести last_name",
            'min_length': "Last name must be no less 2 digits",
            'max_length': "Last name must not be upper 64 digits"
        })
    
    Street_Address = forms.CharField(
        min_length=10,
        max_length=50, 
        label="Street Address",
        error_messages={
            'required': "Street address input required",
            'min_length': "Street address must be no less 5 digits",
            'max_length': "Street address must not be upper 50 digits"
        })
    
    Street_Address_L2 = forms.CharField(
        min_length=5, 
        max_length=50, 
        label="Street Address Line 2",
        error_messages={
            'required': "Street address line 2 input required",
            'min_length': "Street address line 2 must be no less 5 digits",
            'max_length': "Street address line 2 must not be upper 50 digits"
        })
    
    City = forms.CharField(
        min_length=2, 
        max_length=10, 
        label="City",
        error_messages={
            'required': "City input required",
            'min_length': "City must be no less 2 digits",
            'max_length': "City must not be upper 10 digits"
        })
    
    Region = forms.CharField(
        min_length=8, 
        max_length=15, 
        label="Region",
        error_messages={
            'required': "Region input required",
            'min_length': "Region must be no less 8 digits",
            'max_length': "Region must not be upper 15 digits"
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
                
    
    Romania = forms.CharField(label="Ukraine")
    
    Date = forms.CharField(
        label="Date",
        error_messages={
            'required': "Date input required",
        })
    
    Time = forms.CharField(
        label="time",
        error_messages={
            'required': "Time input required",
        })
    is_agree = forms.BooleanField(
        help_text="I accept privacy policy",
        error_messages={
            'required': "You must accept privacy policy"
        }
    )
    
    def clean(self):                               
        cleaned_data = super().clean()
        if 'index' in cleaned_data :
            index = cleaned_data['index']
            if re.search(r"\D", index):
                self.add_error(
                    "index",
                    ValidationError("index must have only digits"))

        if 'Date' in cleaned_data :
            Date = cleaned_data['Date']
            if re.search(r"^\d{2}\.\d{2}\.\d{4}$", Date):
                self.add_error(
                    "Date",
                    ValidationError("Date must be without time"))
        return cleaned_data