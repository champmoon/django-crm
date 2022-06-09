from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Lead


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
