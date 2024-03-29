from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import resolve_url
from django.views import generic

from leads.models import Agent

from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    model = Agent


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return resolve_url('agents:agent-list')

    def form_valid(self, form: ModelForm) -> HttpResponse:
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()

        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Agent
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Agent
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return resolve_url('agents:agent-list')


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Agent
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'

    def get_success_url(self) -> str:
        return resolve_url('agents:agent-list')
