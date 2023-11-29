from time import timezone
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
from .models import Category
from django.conf import settings
DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.core.mail import mail_managers
from django.dispatch import receiver


class CategoryView(View):
     model = Category
     template_name = 'flatpages/category_list.html'
     ordering = ['-name']
     def get (self, request, *args, **kawrgs):
         cat = Category.odjects.get(pk=self.kwargs['pk'])
         queryset = cat.post_set.order_by('-pk')
         return queryset
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['category'] = Category.objects.get(pk=self.kwargs['pk'])
         return context

@login_required()
def subscribe_to(request, pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    if not category.subscribers.filter(pk=user.id).exists():
        category.subscribers.add(user)
        email = user.email
        html = render_to_string( 'flatpages/sub.html',{
            'category': category,
            'user': user
            }
        )
        message = EmailMultiAlternatives(
            subject=f'You have subscribed to the category {category}',
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=[email]
            )

