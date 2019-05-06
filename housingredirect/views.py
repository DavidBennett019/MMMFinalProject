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
            min_rent = int(cleaned_form['min_rent'])
            max_rent = int(cleaned_form['max_rent'])
            relationship = cleaned_form['relationship']
            language = cleaned_form['language']
            rel_prio = int(cleaned_form['rel_prio'])
            lang_prio = int(cleaned_form['lang_prio'])
            pets = 1 if cleaned_form['pets'] == 'Yes' else 0
            if age < 20:
                return render(request, 'error.html', {'errormessage', 'This tool can only provide recommendations for people between 20 and 29 years of age'})
            if max_rent < min_rent:
                return render(request, 'error.html', {'errormessage', 'Your max rent value was less than your min'})
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
            try:
                best_zip = zips[0]
            except:
                return render(request, 'error.html', {'errormessage': 'The zip code you entered was invalid or not in our database, please try another zip code'})
            if cleaned_form['work_zip'] < 1000 or cleaned_form['work_zip'] > 99999:
                return render(request, 'error.html', {'errormessage': 'The zip code you entered was invalid or not in our database, please try another zip code'})
            if zips:
                pass
            else:
                return render(request, 'error.html', {'errormessage': 'The zip code you entered was not in our database, please try another zip code'})
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
                if relationship == 'Male':
                    relval = zr.nev_mar_male_20_34
                elif relationship == 'Female':
                    relval = zr.nev_mar_female_20_34
                elif relationship == 'Either':
                    relval = (zr.nev_mar_female_20_34 + zr.nev_mar_male_20_34) / 2
                else:
                    relval = 0
                if language == 'Spanish':
                    langval = zr.pct_span
                elif language == 'European':
                    langval = zr.pct_euro
                elif language == 'Asian':
                    langval = zr.pct_asia
                else:
                    langval = 0
                utility = genderval * gender_prio + transval * trans_prio + relval * rel_prio + langval * lang_prio - rentval - distanceval
                best_zip = zr if utility > max_utility else best_zip
                max_utility = utility if utility > max_utility else max_utility
            if max_rent > 3000:
                return HttpResponseRedirect('https://www.zillow.com/homes/for_rent/{}/paymenta_sort/{}-_beds/{}_pets'.format(best_zip.zip, beds, pets))
            return HttpResponseRedirect('https://www.zillow.com/homes/for_rent/{}/{}-{}_mp/paymenta_sort/{}-_beds/{}_pets'.format(best_zip.zip, min_rent, max_rent, beds, pets))
    else:
        form = ZipFinderForm()
    return render(request, 'index.html', {'form': form})


def about(request):
    return render(request, 'about.html')

