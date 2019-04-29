from django.db import models

# Create your models here.

class ZipRelation(models.Model):
    zip = models.IntegerField()
    targetID = models.IntegerField()
    distance = models.FloatField()
    one_bed_rent = models.FloatField()
    two_bed_rent = models.FloatField()
    three_bed_rent = models.FloatField()
    four_bed_rent = models.FloatField()
    tot_20_24 = models.IntegerField()
    pct_20_24 = models.FloatField()
    pct_male_20_24 = models.FloatField()
    pct_female_20_24 = models.FloatField()
    tot_25_29 = models.IntegerField()
    pct_25_29 = models.FloatField()
    pct_male_25_29 = models.FloatField()
    pct_female_25_29 = models.FloatField()
    tot_male_20_34 = models.IntegerField()
    nev_mar_male_20_34 = models.FloatField()
    tot_male_35_44 = models.IntegerField()
    nev_mar_male_35_44 = models.FloatField()
    tot_female_20_34 = models.IntegerField()
    nev_mar_female_20_34 = models.FloatField()
    tot_female_35_44 = models.IntegerField()
    nev_mar_female_35_44 = models.FloatField()
    tot_drive = models.FloatField()
    tot_drive_alone = models.FloatField()
    tot_drive_carpool = models.FloatField()
    tot_pub = models.FloatField()
    tot_walk = models.FloatField()
    tot_bike = models.FloatField()
    pct_span = models.FloatField()
    pct_euro = models.FloatField()
    pct_asia = models.FloatField()
    travel_time = models.FloatField()
    unmarried_20_34 = models.FloatField()
    unmarried_35_44 = models.FloatField()




