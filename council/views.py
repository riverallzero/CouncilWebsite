from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
def council(request):
    return render(
        request,
        'council/home.html',
    )

