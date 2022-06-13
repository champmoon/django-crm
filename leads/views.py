from django.shortcuts import resolve_url
from django.views import generic

from .forms import LeadModelForm
from .models import Lead


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


class LeadListView(generic.ListView):
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    model = Lead
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
    form_class = LeadModelForm
    template_name = 'leads/lead_create.html'

    def get_success_url(self) -> str:
        return resolve_url('leads:lead-list')


class LeadUpdateView(generic.UpdateView):
    model = Lead
    form_class = LeadModelForm
    template_name = 'leads/lead_update.html'

    def get_success_url(self) -> str:
        return resolve_url('leads:lead-list')


class LeadDeleteView(generic.DeleteView):
    model = Lead
    template_name = 'leads/lead_delete.html'
    context_object_name = 'lead'

    def get_success_url(self) -> str:
        return resolve_url('leads:lead-list')
