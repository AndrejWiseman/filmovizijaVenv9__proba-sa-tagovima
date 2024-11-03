from django.contrib import admin
from .models import Serije, Epizoda, Filmovi, Category



class FilmoviAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_display = ['title']
    # ordering = ('-date',)




class EpizodaInline(admin.StackedInline):
    model = Epizoda
    extra = 0
    # fields = ['sezona', 'ep', 'epizode_preuzmi', 'epizode_link']
    fields = ['sezona', 'ep']


class SerijeAdmin(admin.ModelAdmin):
    list_display = ['title']
    # ordering = ('-date',)
    prepopulated_fields = {"slug": ("title", )}
    inlines = [EpizodaInline]


# Register your models here.
admin.site.register(Serije, SerijeAdmin)
admin.site.register(Filmovi, FilmoviAdmin)
admin.site.register(Category)




