from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        content = [row for row in reader]

    current_page_number = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(current_page_number)

    context = {
          'bus_stations': page,
          'page': page,
        }
    return render(request, 'stations/index.html', context)
