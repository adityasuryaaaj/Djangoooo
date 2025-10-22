from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=200)
    jurusan = models.CharField(max_length=100)
    angkatan = models.IntegerField()

    def __str__(self):
        return (f"{self.nama}({self.angkatan})")
