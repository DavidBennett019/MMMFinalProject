from .models import ZipRelation
from django import forms


class ZipFinderForm(forms.Form):
    work_zip = forms.IntegerField(label='Work Zip')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Preferred Gender for Roommates', choices=[('Male', 'Male'), ('Female', 'Female'), ('No Preference', 'No Preference')])
    bedrooms = forms.ChoiceField(label='Number of Bedrooms', choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    transportation = forms.ChoiceField(label='Preferred Method of Transportation', choices=[('Driving Alone','Driving Alone'),
                                                                                            ('Carpooling', 'Carpooling'),
                                                                                            ('Public Transit','Public Transit'),
                                                                                            ('Biking', 'Biking'),
                                                                                            ('Walking', 'Walking')])
