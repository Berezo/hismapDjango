from django.shortcuts import render
from django.views.generic.list import ListView

from .models import HistoricalEvent

class HistoricalEventListView(ListView):
    model = HistoricalEvent


    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        return super().get_context_data(
            object_list=queryset.filter(historical_context=self.kwargs['context_id']),
            **kwargs)

# Create your views here.
