from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ZipFinderForm(forms.Form):
    work_zip = forms.IntegerField(label='Work ZIP Code', validators=[MinValueValidator(0), MaxValueValidator(99999)])
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Preferred Gender for Roommates', choices=[('Male', 'Male'), ('Female', 'Female'), ('No Preference', 'No Preference')])
    gender_prio = forms.ChoiceField(label='Priority of Gender Selection (4 highest, 1 lowest)', choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    bedrooms = forms.ChoiceField(label='Number of Bedrooms', choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    transportation = forms.ChoiceField(label='Preferred Method of Transportation', choices=[('Driving Alone','Driving Alone'),
                                                                                            ('Carpooling', 'Carpooling'),
                                                                                            ('Public Transit','Public Transit'),
                                                                                            ('Biking', 'Biking'),
                                                                                            ('Walking', 'Walking')])
    trans_prio = forms.ChoiceField(label='Transportation Method Priority (4 highest, 1 lowest)', choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    pets = forms.ChoiceField(label='Do you have a pet?', choices=[('Yes', 'Yes'), ('No', 'No')])
    min_rent = forms.ChoiceField(label='Minimum Total Monthly Rent', choices=[(0, 0), (500, 500), (750, 750), (1000, 1000),
                                                                 (1250, 1250), (1500, 1500), (1750, 1750), (2000, 2000),
                                                                 (2250, 2250), (2500, 2500), (2750, 2750), (3000, 3000)])
    max_rent = forms.ChoiceField(label='Maximum Total Monthly Rent', choices=[(0, 0), (500, 500), (750, 750), (1000, 1000),
                                                                 (1250, 1250), (1500, 1500), (1750, 1750), (2000, 2000),
                                                                 (2250, 2250), (2500, 2500), (2750, 2750),
                                                                 (3000, 3000), ('', 'Any Price')])
    relationship = forms.ChoiceField(label='Are you looking for a relationship? If so, what gender?', choices=[('Male', 'Yes, male'),
                                                                                                               ('Female', 'Yes, female'),
                                                                                                               ('Either', 'Yes, either'),
                                                                                                                ('No', 'No')])
    rel_prio = forms.ChoiceField(label='Relationship Priority (4 highest, 1 lowest)', choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    language = forms.ChoiceField(label='Do you prefer to live around people who speak languages other than English? If so, which?',
                                 choices=[('Spanish', 'Yes, Spanish'), ('European', 'Yes, other European languages'), ('Asian', 'Yes, Asian languages'),
                                          ('No', 'No')])
    lang_prio = forms.ChoiceField(label='Language Priority (4 highest, 1 lowest)', choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
