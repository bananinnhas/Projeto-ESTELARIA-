from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")


def produtos(request):
    return render(request,"produtos.html")

def detalhes(request):
    return render(request,"detalhes.html")

def quemsomos(request):
    return render(request,"quemsomos.html")
