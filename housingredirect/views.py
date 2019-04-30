from django.shortcuts import render
from .forms import ZipFinderForm
from .models import ZipRelation
from django.http import HttpResponseRedirect

# Create your views here.
# def load_dataset():
#     file = open("C:\\Users\\david\\Documents\\CS4501\\Final Project\\zipfinder\\housingredirect\\Web_Database.csv")
#     df = pd.read_csv(file)
#     for _, row in df.iterrows():
#         new_ziprelation = ZipRelation.objects.create(zip=int(row['Zip']), targetID=int(row['TargetID']), distance=float(row['Distance']),
#                                                      one_bed_rent=float(row['one_bed_rent']), two_bed_rent=float(row['two_bed_rent']),
#                                                      three_bed_rent=float(row['three_bed_rent']), four_bed_rent=float(row['four_bed_rent']),
#                                                      tot_20_24=int(row['Tot20_24']), pct_20_24=float(row['Pct20_24']),
#                                                      pct_male_20_24=float(row['PctMale20_24']),
#                                                      pct_female_20_24=float(row['PctFem20_24']), tot_25_29=int(row['Tot25_29']),
#                                                      pct_25_29=float(row['Pct25_29']), pct_male_25_29=float(row['PctMale25_29']),
#                                                      pct_female_25_29=float(row['PctFem25_29']), tot_male_20_34=int(row['TotMale20_34']),
#                                                      nev_mar_male_20_34=float(row['NevMarMale20_34']), tot_male_35_44=int(row['TotMale35_44']),
#                                                      nev_mar_male_35_44=float(row['NevMarMale35_44']), tot_female_20_34=int(row['TotFem20_34']),
#                                                      nev_mar_female_20_34=float(row['NevMarFem20_34']), tot_female_35_44=int(row['TotFem35_44']),
#                                                      nev_mar_female_35_44=float(row['NevMarFem35_44']), tot_drive=float(row['Tot_Drive']),
#                                                      tot_drive_alone=float(row['Tot_DrvAlone']), tot_drive_carpool=float(row['Tot_DrvCarp']),
#                                                      tot_pub=float(row['Tot_Pub']), tot_walk=float(row['Tot_walk']), tot_bike=float(row['Tot_bike']),
#                                                      pct_span=float(row['PctSpan']), pct_euro=float(row['PctEuro']), pct_asia=float(row['PctAsia']),
#                                                      travel_time=float(row['TravelTime']), unmarried_20_34=float(row['Unmarried20_34']),
#                                                      unmarried_35_44=float(row['Unmarried35_44']))
#         new_ziprelation.save()
#


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
