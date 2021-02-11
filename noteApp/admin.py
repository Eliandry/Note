from django.contrib import admin
from .models import *


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'font')
    search_fields = ('name',)
    save_on_top = True
    list_filter = ('category',)


admin.site.register(Category)


@admin.register(Font)
class FontAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def __str__(self):
        return self.name


