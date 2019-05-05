from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ZipFinderForm(forms.Form):
    work_zip = forms.IntegerField(label='Work ZIP Code', validators=[MinValueValidator(0), MaxValueValidator(99999)])
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Preferred Gender for Roommates', choices=[('Male', 'Male'), ('Female', 'Female'), ('No Preference', 'No Preference')])
    gender_prio = forms.ChoiceField(label='Priority of Gender Selection (3 highest 1 lowest', choices=[(1, 1), (2, 2), (3, 3)])
    bedrooms = forms.ChoiceField(label='Number of Bedrooms', choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    transportation = forms.ChoiceField(label='Preferred Method of Transportation', choices=[('Driving Alone','Driving Alone'),
                                                                                            ('Carpooling', 'Carpooling'),
                                                                                            ('Public Transit','Public Transit'),
                                                                                            ('Biking', 'Biking'),
                                                                                            ('Walking', 'Walking')])
    trans_prio = forms.ChoiceField(label='Priority of Transportation Selection (3 highest 1 lowest)', choices=[(1, 1), (2, 2), (3, 3)])
    pets = forms.ChoiceField(label='Do you have a pet?', choices=[('Yes', 'Yes'), ('No', 'No')])
