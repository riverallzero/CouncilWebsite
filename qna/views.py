from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Qna


# Create your views here.
def qna(request):
    qnas = Qna.objects

    return render(
        request,
        'qna/home.html',
        {'qnas': qnas}
    )


class QnaList(ListView):
    model = Qna
    ordering = "-pk"

    def get_context_data(self, **kwargs):
        context = super(QnaList, self).get_context_data()

        return context


class QnaDetail(DetailView):
    model = Qna

    def get_context_data(self, **kwargs):
        context = super(QnaDetail, self).get_context_data()

        return context