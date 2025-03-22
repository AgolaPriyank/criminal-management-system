from django import forms
from .models import Criminal

class CriminalForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Date picker for Date of Birth
        input_formats=['%Y-%m-%d', '%d/%m/%Y'],  # Accept both 'YYYY-MM-DD' and 'DD/MM/YYYY'
    )
    
    date_of_crime = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y'],  # Accept both 'YYYY-MM-DD' and 'DD/MM/YYYY'
    )
    arrest_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y'],  # Accept both 'YYYY-MM-DD' and 'DD/MM/YYYY'
    )

    class Meta:
        model = Criminal
        fields = [
            'name', 'age', 'date_of_birth', 'gender', 'address', 'city', 'state', 
            'country', 'phone_number', 'aadhaar_number', 'crime_description',
            'date_of_crime', 'arrest_date', 'photo'
        ]
