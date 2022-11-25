from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from notice.forms import QuestionForm
from notice.models import Question

from django.core.paginator import Paginator

from django.views.generic import ListView

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'notice/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'notice/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('notice:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'notice/question_form.html', context)