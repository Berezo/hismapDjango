from django.shortcuts import render
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