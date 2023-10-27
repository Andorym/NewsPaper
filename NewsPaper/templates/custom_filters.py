from django import template

register = template.Library()

stop_words = [
    '�����',
    '����',
    '�����',
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
    print(censor(""" �����1 �����2"""))