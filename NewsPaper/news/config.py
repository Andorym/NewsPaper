from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def newsletter_sender(list_recipients, category, posts):

    html_content = render_to_string(
        'templates/account/sender_create.html',
        {'posts': posts, }
    )

    msg = EmailMultiAlternatives(
        subject=f'NewsPaper. ������� �� ������ � ��������� {category}.',
        body=f'������:',
        to=list_recipients
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()