from django.shortcuts import render

# Create your views here.
def cafe(request):
    return render(
        request,
        'partnership/home.html',
    )

def convenience(request):
    return render(
        request,
        'partnership/Convenience.html',
    )
def food(request):
    return render(
        request,
        'partnership/food.html',
    )

def bar(request):
    return render(
        request,
        'partnership/bar.html',
    )

def index_cafe(request):
    return render(
        request,
        'location/index_cafe.html',
    )

def index_convenience(request):
    return render(
        request,
        'location/index_convenience.html',
    )