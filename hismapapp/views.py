from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import HistoricalEvent
from .forms import HistoricalEventForm

# Create your views here.

class HistoricalEventListView(ListView):
    model = HistoricalEvent

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        return super().get_context_data(
            object_list=queryset.filter(historical_context=self.kwargs['context_id']),
            **kwargs)


class HistoricalEventCreateView(CreateView):
    model = HistoricalEvent
    form_class = HistoricalEventForm

class HistoricalEventUpdateView(UpdateView):
    model = HistoricalEvent
    form_class = HistoricalEventForm

def geojson(request, context_id):
    model = HistoricalEvent
    data = serialize('geojson', model.objects.filter(historical_context=context_id), geometry_field='geometry')
    return HttpResponse(data, content_type = 'application/geo+json')