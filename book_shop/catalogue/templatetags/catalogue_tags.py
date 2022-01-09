from django import template
from catalogue.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('catalogue/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
