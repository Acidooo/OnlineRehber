from .models import Contact
from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class ContactAdmin(ImportExportModelAdmin):

    list_display = ('id','isim','soyisim','email','telefon','cinsiyet','bilgi','etiket')
    list_editable = ('telefon','bilgi',)
    list_display_links = ('isim', 'soyisim', 'email', 'cinsiyet',)
    list_per_page = 20
    search_fields = ('isim','soyisim','email','telefon','cinsiyet','bilgi')
    list_filter = ('cinsiyet','ekl_tarih','etiket')


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)