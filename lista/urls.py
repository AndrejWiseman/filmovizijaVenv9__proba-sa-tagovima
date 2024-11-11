from django.urls import path
# from .views import ListaListView
from lista.views import ArticleListView

urlpatterns = [
    path('article-list/', ArticleListView.as_view(), name="article-list"),
]
