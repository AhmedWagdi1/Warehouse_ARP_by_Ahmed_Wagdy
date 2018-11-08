from django import template
from django.db.models import Sum, Q


register = template.Library()

@register.filter
def annot_far3y(value):
    print(value)
    return value.annotate(total_da2en=Sum('da2en'))
