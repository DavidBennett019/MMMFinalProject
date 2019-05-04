from django.shortcuts import render
from .forms import ZipFinderForm
from .models import ZipRelation
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = ZipFinderForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            zips = ZipRelation.objects.filter(targetID=cleaned_form['work_zip'])
            max_utility = float('-inf')
            best_zip = zips[0]
            age = cleaned_form['age']
            gender = cleaned_form['gender']
            trans = cleaned_form['transportation']
            beds = cleaned_form['bedrooms']
            for zr in zips:
                distanceval = zr.distance
                if gender == 'Male':
                    genderval = zr.pct_male_20_24 if 20 <= age <= 24 else zr.pct_male_25_29
                elif gender == 'Female':
                    genderval = zr.pct_female_20_24 if 20 <= age <= 24 else zr.pct_female_25_29
                else:
                    genderval = (zr.pct_male_20_24 + zr.pct_female_20_24) / 2 if 20 <= age <= 24 else (zr.pct_male_25_29 + zr.pct_female_25_29) / 2
                if trans == 'Drive Alone':
                    transval = zr.tot_drive_alone
                elif trans == 'Carpool':
                    transval = zr.tot_carpool
                elif trans == 'Public Transit':
                    transval = zr.tot_pub
                elif trans == 'Walk':
                    transval = zr.tot_walk
                else:
                    transval = zr.tot_bike
                if beds == 1:
                    rentval = zr.one_bed_rent
                elif beds == 2:
                    rentval = zr.two_bed_rent
                elif beds == 3:
                    rentval = zr.three_bed_rent
                else:
                    rentval = zr.four_bed_rent
                utility = genderval + transval - rentval - distanceval
                best_zip = zr if utility > max_utility else best_zip
                max_utility = utility if utility > max_utility else max_utility
                print(best_zip)
            return HttpResponseRedirect('https://www.zillow.com/homes/for_rent/{}/paymenta_sort/{}-_beds/'.format(best_zip.zip, beds))
    else:
        form = ZipFinderForm()
    return render(request, 'index.html', {'form': form})
