from django.shortcuts import render

# Create your views here.
def council(request):
    return render(
        request,
        'council/home.html',
    )