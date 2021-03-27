from django.shortcuts import render, get_object_or_404


from front.models import Category, News, Tags


def index(req):
    print('ya zapustilsya')
    return render(req, 'front/base_olya.html', context={
        'category_0':  Category.objects.filter(parent=None) ,
        'tegs ': Tags.objects.filter(id= 1)
    })


def category_list(request, **kwargs):

    if 'pk' in kwargs:
        c = get_object_or_404(Category, pk=kwargs['pk'] )
    elif 'slug' in kwargs:
        c = Category.objects.get(name=kwargs['slug'])

    return render(request, 'front/category_list.html', {'cat': c})


def text(req ,**kwargs):
    if 'pk' in kwargs:
        text = get_object_or_404(News, pk=kwargs['pk'])
    return render(req, 'front/post_detail.html', {'text':text})


def tegs (req , **kwargs):
    if 'slug' in kwargs:
        tag = Tags.objects.get(tags = kwargs['slug'])
    return render(req, 'front/tegs.html', {'teg': tag})






