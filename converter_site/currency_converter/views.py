from datetime import datetime, time, timedelta

import requests
from bs4 import BeautifulSoup
from django.db.models import Max
from django.forms import forms
from django.shortcuts import render
from django.utils.timezone import now

from .forms import ConverterForm
from .models import Rate


# Create your views here.

def update_rate():
    r = requests.get("https://www.cbr.ru/currency_base/daily/")
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table', class_='data').find_all('tr')

        for cur in table:
            cur = cur.find_all('td')
            if len(cur) != 0:
                rubles = float(cur[4].text.replace(',', '.')) / float(cur[2].text.replace(',', '.'))
                currency = cur[1].text
                if Rate.objects.filter(currency=currency).count() == 0:
                    Rate.objects.create(currency=currency, rubles=rubles)
                else:
                    rate = Rate.objects.get(currency=currency)
                    rate.rubles = rubles
                    rate.save()


def check_last_update():
    return now() - Rate.objects.aggregate(Max('updated'))['updated__max']


def converter_page(request):
    last_update = check_last_update()
    if last_update > timedelta(minutes=5):
        update_rate()
        hours, minutes, seconds = 0, 0, 0
    else:
        hours = last_update.seconds // 3600
        minutes = (last_update.seconds // 60) % 60
        seconds = round(last_update.seconds % 60)

    if request.method == "GET":
        form = ConverterForm()
        answer = ""
    if request.method == "POST":
        form = ConverterForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

        from_rate = Rate.objects.get(currency=form_data['from_currency'])
        to_rate = Rate.objects.get(currency=form_data['to_currency'])
        answer = str(round(form_data['value'] * from_rate.rubles / to_rate.rubles, 3))

    return render(request, 'index.html', {'form': form, 'answer': answer, 'hours': hours, 'minutes': minutes, 'seconds': seconds})
