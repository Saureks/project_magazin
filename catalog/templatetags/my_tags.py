from django import template

register = template.Library()


@register.simple_tag()
def mymedia(val):
    if val:
        return f"/media/{val}"
    return "#"