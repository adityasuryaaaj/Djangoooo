from django.shortcuts import render
from .models import Mahasiswa

def home(request):
    context ={
        "nama":"Aditya",
        "umur": 27,
        "hobi":["coding","baca","gaming"],
       
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def daftar_siswa(request):
    data = Mahasiswa.objects.all().order_by("-angkatan")
    return render(request,"daftar_siswa.html",{"data":data})