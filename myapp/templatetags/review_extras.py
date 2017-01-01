from django import template
from django.template.defaultfilters import stringfilter
from myapp.models import Author
from datetime import datetime

register = template.Library()


def cut(value, arg):
    return value.replace(arg, '')


def lower(value):  # Only one argument
    return value.lower()


register.filter("cur", cut)
register.filter('lower', lower)


# You can use register.filter() as s decorator instead
@register.filter(name="cut")
def cut(value, arg):
    return value.replace('arg', '')


@register.filter
@stringfilter
def lower(value):
    return value.lower()


@register.filter(is_safe=True)
def myfilter(value):
    return value


@register.filter(is_safe=True)
def add_xx(value):
    return "{}xx".format(value)


@register.filter
def hack(value):
    return value.replace('a', 'A')


@register.inclusion_tag('myapp/tag_test.html')
def authorList():
    authors = Author.objects.all()
    return {'authors': authors}

@register.simple_tag
def current_time(*args):
    return datetime.now()
