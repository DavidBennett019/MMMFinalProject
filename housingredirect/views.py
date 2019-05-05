from django.shortcuts import render
from .forms import ZipFinderForm
from .models import ZipRelation
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = ZipFinderForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            age = cleaned_form['age']
            gender = cleaned_form['gender']
            trans = cleaned_form['transportation']
            beds = cleaned_form['bedrooms']
            gender_prio = int(cleaned_form['gender_prio'])
            trans_prio = int(cleaned_form['trans_prio'])
            pets = 1 if cleaned_form['pets'] == 'Yes' else 0
            if age > 29:
                return HttpResponseRedirect('https://www.aarp.org/')
            if trans == 'Walk':
                zips = ZipRelation.objects.filter(targetID=cleaned_form['work_zip'], distance__lte=2500)
            elif trans == 'Bike':
                zips = ZipRelation.objects.filter(targetID=cleaned_form['work_zip'], distance__lte=8000)
            else:
                zips = ZipRelation.objects.filter(targetID=cleaned_form['work_zip'])
            if zips:
                pass
            else:
                zips = ZipRelation.objects.filter(targetID=cleaned_form['work_zip'])
            max_utility = float('-inf')
            best_zip = zips[0]
            if cleaned_form['work_zip'] < 1000 or cleaned_form['work_zip'] > 99999:
                return render(request, 'error.html', {'errormessage': 'This zip code was either invalid or not in our database, please enter a valid zip code'})
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
                    rentval = zr.two_bed_rent / 2
                elif beds == 3:
                    rentval = zr.three_bed_rent / 3
                else:
                    rentval = zr.four_bed_rent / 4
                utility = genderval * gender_prio + transval * trans_prio - rentval - distanceval
                best_zip = zr if utility > max_utility else best_zip
                max_utility = utility if utility > max_utility else max_utility
            return HttpResponseRedirect('https://www.zillow.com/homes/for_rent/{}/paymenta_sort/{}-_beds/{}_pets'.format(best_zip.zip, beds, pets))
    else:
        form = ZipFinderForm()
    return render(request, 'index.html', {'form': form})

def about(request):
    return render(request, 'about.html')
