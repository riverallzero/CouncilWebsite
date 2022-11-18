from django.shortcuts import render
from .models import Notice
from django.views.generic import ListView, DetailView


# Create your views here.
def notice(request):
    notices = Notice.objects

    return render(
        request,
        'notice/home.html',
        {'notices': notices}
    )


class NoticeList(ListView):
    model = Notice
    ordering = "-pk"

    def get_context_data(self, **kwargs):
        context = super(NoticeList, self).get_context_data()

        return context


class NoticeDetail(DetailView):
    model = Notice

    def get_context_data(self, **kwargs):
        context = super(NoticeDetail, self).get_context_data()

        return context
