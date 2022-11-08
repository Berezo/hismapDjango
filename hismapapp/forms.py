from django.contrib.gis import forms
from .models import HistoricalEvent

class HistoricalEventForm(forms.ModelForm):
    geometry = forms.PointField(required=False, widget=forms.OSMWidget(attrs={'map_width': 1300, 'map_height': 500, 'template_name': 'gis/openlayers-osm.html', 'default_lat': 50.89, 'default_lon': 10.88, 'default_zoom': 6}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        for field in iter(self.fields):
            if field != 'typ':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-select'
                })
    
    class Meta:
        model = HistoricalEvent
        fields = ('ogc_fid','name','date', 'description', 'belligerent_1', 'belligerent_2', 'commander_1', 'commander_2', 'strength_1', 'strength_2', 'result', 'historical_context', 'geometry')
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Field is required.'}),
            'date': forms.TextInput(attrs = {'class': 'form-control'}),
            'description': forms.TextInput(attrs = {'class': 'form-control'}),
            'belligerent_1': forms.TextInput(attrs = {'class': 'form-control'}),
            'belligerent_2': forms.TextInput(attrs = {'class': 'form-control'}),
            'commander_1': forms.TextInput(attrs = {'class': 'form-control'}),
            'commander_2': forms.TextInput(attrs = {'class': 'form-control'}),
            'strength_1': forms.TextInput(attrs = {'class': 'form-control'}),
            'strength_2': forms.TextInput(attrs = {'class': 'form-control'}),
            'result': forms.TextInput(attrs = {'class': 'form-control'}),
            'historical_context': forms.Select(attrs = {'class': 'form-select'}),
            'geometry': forms.OSMWidget(attrs={'map_width': 1300, 'map_height': 500, 'template_name': 'gis/openlayers-osm.html', 'default_lat': 50.89, 'default_lon': 10.88, 'default_zoom': 6}),
        }
