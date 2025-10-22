from django.contrib import admin
from .models import Mahasiswa

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ("nama","jurusan","angkatan")
    search_fields = ("nama","jurusan")
    list_filter = ("jurusan","angkatan")
