from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm
from .models import Question

from django.core.paginator import Paginator


def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'survey/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'survey/question_detail.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('survey:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'survey/question_form.html', context)