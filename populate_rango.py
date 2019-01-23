import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_jdango_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 225},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 444},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views": 378}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 882},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 2023},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 7765}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 492},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 3748}]

    cats = {"Python": {"pages": python_pages, "views": 1014, "likes": 464},
            "Django": {"pages": django_pages, "views": 10670, "likes": 3299},
            "Other Frameworks": {"pages": other_pages, "views": 4240, "likes": 882}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],  p["views"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()