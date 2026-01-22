from django.db import models

class Pendaftar(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nama
class Negara(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Provinsi(models.Model):
    negara = models.ForeignKey(Negara, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Kabupaten(models.Model):
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
