from django import template
from lessons.models import LessonType
import random

register = template.Library()

@register.filter(name='types')
def types(value,key):
    if value is None:
        value = ' '
    lessons = LessonType.objects.all().exclude(id=key)
    return lessons

@register.filter(name='times')
def times(number):
    if number is None:
        number = 1
    return range(number)


@register.filter(name='shuffle')
def shuffle(arg):
    random.seed(0)
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp


@register.filter(name='trim')
def trim(value, keys):
    if value is None:
        value = 'khj,jhkgh,k'
    for key in keys:
        value = value.strip(key)
    return value


@register.filter(name='split')
def split(value, key):
    """
    Returns the value turned into a list.
  """
    if value is None:
        value = ' '
    return value.split(key)


@register.filter(name='containGroup')
def containGroup(query, value):
    """
    Returns the value turned into a list.
  """
    if value is None:
        value = ' '

    check = any(value == group.name for group in query)
    if check:
        return True
    else:
        return False

# @register.filter(name='merge2')
# def merge2(list1, list2):
#   """
#     Returns the value turned into a list.
#   """
#   if list1 is None or list2 is None:
#     list1=[]
#     list2= []
#   return list1+list2
