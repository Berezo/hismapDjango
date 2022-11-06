from django.contrib.gis import forms
from .models import HistoricalEvent

class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = HistoricalEvent
        fields = ('ogc_fid','name','date', 'description', 'belligerent_1', 'belligerent_2', 'commander_1', 'commander_2', 'strength_1', 'strength_2', 'result', 'historical_context', 'geometry')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True