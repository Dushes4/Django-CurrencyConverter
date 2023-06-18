from django.db import models


# Create your models here.

class Rate(models.Model):
    CURRENCIES = (('AUD', 'AUD'), ('AZN', 'AZN'), ('AMD', 'AMD'), ('BYN', 'BYN'), ('BGN', 'BGN'), ('BRL', 'BRL'),
                  ('HUF', 'HUF'), ('KRW', 'KRW'), ('VND', 'VND'), ('HKD', 'HKD'), ('GEL', 'GEL'), ('DKK', 'DKK'),
                  ('AED', 'AED'), ('USD', 'USD'), ('EUR', 'EUR'), ('EGP', 'EGP'), ('INR', 'INR'), ('IDR', 'IDR'),
                  ('KZT', 'KZT'), ('CAD', 'CAD'), ('QAR', 'QAR'), ('KGS', 'KGS'), ('CNY', 'CNY'), ('MDL', 'MDL'),
                  ('NZD', 'NZD'), ('TMT', 'TMT'), ('NOK', 'NOK'), ('PLN', 'PLN'), ('RON', 'RON'), ('XDR', 'XDR'),
                  ('RSD', 'RSD'), ('SGD', 'SGD'), ('TJS', 'TJS'), ('THB', 'THB'), ('TRY', 'TRY'), ('UZS', 'UZS'),
                  ('UAH', 'UAH'), ('GBP', 'GBP'), ('CZK', 'CZK'), ('SEK', 'SEK'), ('CHF', 'CHF'), ('ZAR', 'ZAR'),
                  ('JPY', 'JPY'), ('RUB', 'RUB'))

    currency = models.CharField(blank=False, choices=CURRENCIES, max_length=3)
    rubles = models.FloatField(blank=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency
