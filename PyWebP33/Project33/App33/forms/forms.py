from django import forms


class TaxiCarForm(forms.Form):

    BRAND_CHOICES =\
    [
        ('', 'Select brand'),
        ('toyota', 'Toyota'),
        ('honda', 'Honda'),
        ('hyundai', 'Hyundai'),
        ('other', 'Other')
    ]

    COLOR_CHOICES =\
    [
        ('', 'Select color'),
        ('white', 'White'),
        ('black', 'Black'),
        ('silver', 'Silver'),
        ('gray', 'Gray')
    ]

    brand = forms.ChoiceField(
        choices=BRAND_CHOICES,
        label='Car Brand',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    model = forms.CharField(
        max_length=50,
        label='Model',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    license_plate = forms.CharField(
        max_length=10,
        label='License Plate',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'AA1234BB'
        })
    )

    year = forms.IntegerField(
        min_value=2000,
        max_value=2025,
        label='Year',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '2025'
        })
    )

    color = forms.ChoiceField(
        choices=COLOR_CHOICES,
        label='Color',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    driver_name = forms.CharField(
        max_length=100,
        label='Driver Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    def clean_license_plate(self):
        license_plate = self.cleaned_data['license_plate']
        license_plate = license_plate.upper().replace(' ', '')

        if len(license_plate) < 6:
            raise forms.ValidationError('license plate is too short')

        return license_plate