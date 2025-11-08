from django import forms

class DemoForm(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=64, label="Name")
    last_name = forms.CharField(min_length=2, max_length=64, label="Surname")