
from django import template

from core.models import Blog

register = template.Library()


@register.simple_tag

def get_blogs(offset, limit, order_by, words=None, truncate=None):
    
    if order_by == 0:
        return Blog.objects.filter(is_active=True).order_by('-created_at')[offset,limit]
    return Blog.objects.filter(is_active=True).order_by('-created_at')[offset,limit]