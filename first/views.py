from django.shortcuts import render

# Create your views here.

def one(request):
    return render(request, 'first/one.html')


def two(request):
    return render(request, 'first/two.html')


def three(request):
    return render(request, 'first/three.html')