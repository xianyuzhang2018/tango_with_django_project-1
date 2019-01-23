from django.shortcuts import render
from rango.models import Category
from rango.models import Page



def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pagelist': page_list,}

    return render(request, 'rango/index.html', context_dict)


def about(request):

    context_dict = {'boldmessage': "Hey!"}

    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)

def show_page(request):
    context_dict = {}

    try:
        pagelist = Page.objects.get(Category.objects.all())
        context_dict['pagelist'] = pagelist
    except Category.DoesNotExist:
        context_dict['pageslist'] = None

    return render(request, context_dict)