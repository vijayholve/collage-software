# your_app/templatetags/custom_tags.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')

# You can also create custom template tags using the @register.simple_tag decorator.
@register.simple_tag
def custom_tag_example(arg1, arg2):
    return f'{arg1} and {arg2}'
