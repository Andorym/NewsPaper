from unittest import result
from django import template

register = template.Library()

stop_words = [
    'Дурак',
    'Идит',
    'Бебей',
 ]

@register.filter(name = 'preview')
def preview(value):
    if len(value) > 50:
        return value[:51] + '...'
    else:
        return value

@register.lilter(name='censor')
def censor(value):
    for sw in stop_words:
        value = value.lower().replace(sw.lower(), '...')
        return value


if __name__ == '__main__':
    print(censor(""" Слово1 слово2"""))

@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in stop_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)
