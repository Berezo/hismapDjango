from django.contrib.gis.db import models

class HistoricalContext(models.Model):
    class Meta:
        db_table = 'historical_context'
        ordering = ['name']
        
    name = models.CharField(blank=True, null=True, max_length=80)
    period_start = models.CharField(blank=True, null=True, max_length=80)
    period_end = models.CharField(blank=True, null=True, max_length=80)
    description = models.CharField(blank=True, null=True, max_length=254)
    
    def __str__(self):
        return f'{self.name}'

class HistoricalEvent(models.Model):
    class Meta:
        db_table = 'historical_event'
        ordering = ['date']
    
    ogc_fid = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(blank=True, null=True, max_length=80)
    historical_context = models.ForeignKey(HistoricalContext, models.PROTECT, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=254)
    belligerent_1 = models.CharField(blank=True, null=True, max_length=254)
    belligerent_2 = models.CharField(blank=True, null=True, max_length=254)
    commander_1 = models.CharField(blank=True, null=True, max_length=254)
    commander_2 = models.CharField(blank=True, null=True, max_length=254)
    strength_1 = models.CharField(blank=True, null=True, max_length=254)
    strength_2 = models.CharField(blank=True, null=True, max_length=254)
    result = models.CharField(blank=True, null=True, max_length=254)
    geometry = models.PointField(srid=3857, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'


