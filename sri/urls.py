from django.urls import path
from .views import daftar, sukses

app_name = 'sri'

urlpatterns = [
    path('pendaftaran/', daftar, name='daftar'),
    path('pendaftaran/sukses/', sukses, name='sukses'),
]
