from django.shortcuts import render

# Create your views here.
def partnership(request):
    return render(
        request,
        'partnership/home.html',
    )