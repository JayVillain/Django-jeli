from django.contrib import admin
from .models import Negara, Provinsi, Kabupaten, Pendaftar

admin.site.register(Negara)
admin.site.register(Provinsi)
admin.site.register(Kabupaten)
admin.site.register(Pendaftar)
