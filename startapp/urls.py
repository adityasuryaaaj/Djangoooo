from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('siswa/',views.daftar_siswa,name='siswa'),
]