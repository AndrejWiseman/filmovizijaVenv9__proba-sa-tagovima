from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.utils import timezone
from django.views.generic.list import ListView

from home.models import Filmovi, Serije

# Create your views here.
class ArticleListView(ListView):
    # template_name = "spisak.html"

    model = Filmovi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

