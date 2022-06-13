from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import LeadModelForm
from .models import Agent, Lead


def lead_list(request: HttpRequest) -> HttpResponse:
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads/lead_list.html', context)


def lead_detail(request: HttpRequest, pk: int) -> HttpResponse:
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request: HttpRequest) -> HttpResponse:
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)


def lead_update(request: HttpRequest, pk: int) -> HttpResponse:
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/lead_update.html', context)


def lead_delete(request: HttpRequest, pk: int) -> HttpResponse:
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')
