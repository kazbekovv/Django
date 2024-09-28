from django.shortcuts import render
from django.views.generic import ListView, FormView
from parser.models import TVParser
from parser.forms import ParserForm
from django.http import HttpResponse


class FilmListView(ListView):
    model = TVParser
    template_name = 'parser/film_list.html'

    def get_queryset(self):
        return TVParser.objects.all()

class ParserView(FormView):
    template_name = "parser/start_parsing.html"
    form_class = ParserForm

    def post(self, request, *args, **kwargs):
        form = ParserForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        form.parser_data()
        return HttpResponse("OK")