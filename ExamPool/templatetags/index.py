from django import template
register = template.Library()

@register.filter
def index(List, i):
    print(i)
    return List[int(i)]

@register.filter
def maxTag(Names, Counts):
    return Names[Counts.index(max(Counts))]