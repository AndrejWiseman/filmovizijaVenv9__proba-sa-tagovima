from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from itertools import chain
from operator import attrgetter
from django.core.paginator import Paginator
from .models import Filmovi, Serije, Category

# Create your views here.
def index(request, category_slug=None):

    category = None
    categories = Category.objects.all()

    filmovi = Filmovi.objects.all()
    serije = Serije.objects.all()



    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        filmovi = filmovi.filter(category=category)
        serije = serije.filter(category=category)


    # queryset = sorted(chain(filmovi, serije), key=lambda x: x.date, reverse=True)[:6]
    queryset = list(filmovi) + list(serije)

    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'queryset': queryset,

        'category': category,
        'categories': categories,
        'filmovi': filmovi,
        'serije': serije,
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context)



### stari nacin valja ###
def filmovi(request, category_slug=None):

    filmovi = Filmovi.objects.all().order_by('-date')

    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        filmovi = filmovi.filter(category=category)

    paginator = Paginator(filmovi, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)


    context = {
        'filmovi': filmovi,
        'categories': categories,
        'category': category,
        'page_obj': page_obj,

    }
    return render(request, 'filmovi.html', context)



def filmovi_detaljno(request, slug):

    f_detaljno = get_object_or_404(Filmovi, slug=slug)

    context = {
        'f_detaljno': f_detaljno,
    }
    return render(request, 'film-detaljno.html', context)




##### stari nacin valja #######
def serije(request):

    serije = Serije.objects.all().order_by('-date')

    categories = Category.objects.all()

    context = {
        'serije': serije,
        'categories': categories,
    }
    return render(request, 'serije.html', context)


def serije_detaljno(request, slug):

    s_setaljno = get_object_or_404(Serije, slug=slug)
    # epizode = s_setaljno.get_episodes()

    epizode_po_sezoni = s_setaljno.get_episodes_by_season()

    context = {
        's_setaljno': s_setaljno,
        'epizode_po_sezoni': epizode_po_sezoni,
    }
    return render(request, 'serije-detaljno.html', context)





def pocetnaLista(request):

    context = {

    }
    return render(request, 'pocetna-lista.html', context)

