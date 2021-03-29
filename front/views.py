
from django.views.generic import ListView, DetailView

from front.models import Category, News, Tags


class HomeView(ListView):
    model = Category
    template_name = 'front/base.html'
    context_object_name = 'Category'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Blog news'
        return context

    def get_queryset(self):
        return Category.objects.filter(parent=None)


class News_list(ListView):
    model = News
    template_name = 'front/index.html'
    context_object_name = 'catlist'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return News.objects.filter(categori__name=self.kwargs['slug'])



class Text(DetailView):
    model = News
    template_name = 'front/post_detail.html'
    context_object_name = 'text'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Tegs (DetailView):
    model =  Tags
    template_name = 'front/tegs.html'
    context_object_name = 'teg'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Tags.objects.filter(news__tags__news=self.kwargs['pk'])












