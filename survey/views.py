from django.shortcuts import render
from .models import Survey
from django.views.generic import ListView, DetailView


# Create your views here.
def survey(request):
    surveys = Survey.objects
    return render(
        request,
        'survey/home.html',
        {'surveys': surveys}
    )


class SurveyList(ListView):
    model = Survey
    ordering = "-pk"

    def get_context_data(self, **kwargs):
        context = super(SurveyList, self).get_context_data()

        return context


class SurveyDetail(DetailView):
    model = Survey

    def get_context_data(self, **kwargs):
        context = super(SurveyDetail, self).get_context_data()

        return context