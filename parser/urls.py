from django.urls import path
from parser.views import ParserView, FilmListView

urlpatterns = [
    path("parsing/", ParserView.as_view(), name="parser"),
    path("films/", FilmListView.as_view(), name="films"),
]