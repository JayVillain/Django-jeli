from django.contrib import admin
from .models import (
    Negara, Provinsi, Kabupaten,
    Kecamatan, Desa, Pendaftar
)

admin.site.register(Negara)
admin.site.register(Provinsi)
admin.site.register(Kabupaten)
admin.site.register(Kecamatan)
admin.site.register(Desa)
admin.site.register(Pendaftar)
