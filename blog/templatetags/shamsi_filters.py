import jdatetime
from django import template

register = template.Library()

@register.filter
def to_shamsi(value):
    if not value:
        return ""
    return jdatetime.datetime.fromgregorian(datetime=value).strftime('%Y/%m/%d')
