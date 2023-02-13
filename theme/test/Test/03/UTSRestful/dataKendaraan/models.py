from django.db import models

# Create your models here.
class Kendaraan(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    no_polisi = models.CharField(max_length=10)
    warna = models.CharField(max_length=10)
    merk = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    jenis = models.CharField(max_length=20)
    tahun = models.DateField()
    pajak = models.IntegerField(max_length=50)
    release_date = models.DateTimeField()
class Meta:
    ordering = ('no_polisi',)