from django.urls import path
from .views import index, pocetnaLista, filmovi, filmovi_detaljno, serije, serije_detaljno

urlpatterns = [
    path('', index, name='home'),

    path('category/<slug:category_slug>/', index, name='category' ),
    path('filmovi/', filmovi, name='filmovi'),
    path('filmovi/<slug:slug>', filmovi_detaljno, name='film-detaljno'),
    path('serije/', serije, name='serije'),
    path('serije/<slug:slug>', serije_detaljno, name='serija-detaljno'),

    # path('', pocetnaLista, name='home'),
]
