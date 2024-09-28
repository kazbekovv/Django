from django.contrib import admin
from parser.models import TVParser

@admin.register(TVParser)
class TVParserAdmin(admin.ModelAdmin):
    list_display = ('title_url', 'title_name', 'image')
    search_fields = ['title_name']

