from django import template
register = template.Library()

@register.filter
def index(List, i):
    print(i)
    return List[int(i)]

@register.filter
def maxTag(Names, Counts):
    return Names[Counts.index(max(Counts))]

@register.filter
def keyToValue(Dict, Key):
    return Dict[Key]

@register.filter
def subtract(val1, val2):
    return val1 - val2