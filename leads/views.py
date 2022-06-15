from django.core.mail import send_mail
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .forms import CustomUserCreationForm, LeadModelForm
from .models import Lead


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return resolve_url('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, generic.ListView):
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    model = Lead
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = LeadModelForm
    template_name = 'leads/lead_create.html'

    def get_success_url(self) -> str:
        return resolve_url('leads:lead-list')

    def form_valid(self, form: ModelForm) -> HttpResponse:
        send_mail(
            subject='A lead has been created',
            message='Go to the site to see the new lead',
            from_email='test@test.com',
            recipient_list=['recip1@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Lead
    form_class = LeadModelForm
    template_name = 'leads/lead_update.html'

    def get_success_url(self) -> str:
        return resolve_url('leads:lead-list')


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Lead
    template_name = 'leads/lead_delete.html'
    context_object_name = 'lead'

    def get_success_url(self) -> str:
        return resolve_url('leads:lead-list')
