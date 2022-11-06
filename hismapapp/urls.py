from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import path, reverse_lazy
from .models import HistoricalContext, HistoricalEvent


urlpatterns = [
    path('hiscontext/list/',
         ListView.as_view(
             model=HistoricalContext,
             template_name='historicalcontext_list.html'
          ),
         name='hiscontext-list'),
    path('hiscontext/create/',
         CreateView.as_view(
            model=HistoricalContext,
            fields='__all__',
            success_url=reverse_lazy('hismapapp:hiscontext-list'),
            template_name='generic_update.html'
         ),
         name='hiscontext-create'),
    path('hiscontext/<int:pk>/edit/',
         UpdateView.as_view(
            model=HistoricalContext,
            fields='__all__',
            success_url=reverse_lazy('hismapapp:hiscontext-list'),
            template_name='generic_update.html'
         ),
         name='hiscontext-edit'),
    path('hiscontext/<int:pk>/delete/',
         DeleteView.as_view(
            model=HistoricalContext,
            success_url=reverse_lazy('hismapapp:hiscontext-list'),
            template_name='generic_delete.html'
         ),
         name='hiscontext-delete'),
    
    path('hisevent/list/',
         ListView.as_view(
             model=HistoricalEvent,
             template_name='historicalevent_list.html'
          ),
         name='hisevent-list'),
    path('hisevent/create/',
         CreateView.as_view(
            model=HistoricalEvent,
            fields='__all__',
            success_url=reverse_lazy('hismapapp:hisevent-list'),
            template_name='generic_update.html'
         ),
         name='hisevent-create'),
    path('hisevent/<int:pk>/edit/',
         UpdateView.as_view(
            model=HistoricalEvent,
            # pk_url_kwarg = 'ogc_fid',
            fields='__all__',
            success_url=reverse_lazy('hismapapp:hisevent-list'),
            template_name='generic_update.html'
         ),
         name='hisevent-edit'),
    path('hisevent/<int:pk>/delete/',
         DeleteView.as_view(
            model=HistoricalEvent,
            success_url=reverse_lazy('hismapapp:hisevent-list'),
            template_name='generic_delete.html'
         ),
         name='hisevent-delete'),
]
