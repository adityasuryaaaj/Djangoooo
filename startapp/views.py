from django.shortcuts import render

def home(request):
    context ={
        "nama":"Aditya",
        "umur": 27,
        "hobi":["coding","baca","gaming"],
       
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')