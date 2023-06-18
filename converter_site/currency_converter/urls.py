from django.urls import path

from .views import converter_page

urlpatterns = [
    path('', converter_page),
]
