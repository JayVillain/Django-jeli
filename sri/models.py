from django.db import models

class Pendaftar(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nama
