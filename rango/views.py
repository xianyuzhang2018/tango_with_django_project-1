from django.shortcuts import render
from rango.models import Category
from rango.models import Page



def index(request):

    # no. likes, in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    category_list = Category.objects.order_by('-likes')[:5]
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


def about(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Hey!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    #create a context dictionary which we can [ass to the tamplate rendering engine
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
