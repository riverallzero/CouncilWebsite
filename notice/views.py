from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect



class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields= ['title', 'content', 'head_image', 'file_upload',]

    template_name = 'notice/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()

        return context

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)

        return response


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload',]

    template_name = 'notice/post_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)

            return response
        else:
            return redirect('/notice/')


class PostList(ListView):
    model = Post
    ordering = "-pk"

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()

        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()

        return context


def post_delete(request, pk):
    question = get_object_or_404(Post, pk=pk)
    question.delete()
    return redirect('notice:index')

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.order_by('-created_at')
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    return render(request, 'notice/post_list.html', context)