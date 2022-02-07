from django.http import HttpResponse
from django.shortcuts import render
# from combaterincendio.models import

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import datetime

from django.views.generic.edit import CreateView
from combaterincendio.forms import AskForFormCaptcha
from django.views.generic import TemplateView
from combaterincendio.models import Servico, Diferencial, Clientes, Blog, BlogCategory, \
    Empresas, SiteContact
from django.http import HttpResponseRedirect, HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.filter(ativo=True)
        context['diferencial'] = Diferencial.objects.filter(ativo=True)
        context['clientes'] = Clientes.objects.filter(ativo=True)
        context['articles'] = Blog.objects.filter(show_home=True)
        context['empresas'] = Empresas.objects.filter(featured=True)
        context['contact_form'] = AskForFormCaptcha()
        return context


def blog(request):
    context = {}

    articles = Blog.objects.all()
    context['articles'] = articles

    context['categories'] = BlogCategory.objects.all()

    return render(request, 'blog.html', context)


def blog_page(request, slug):
    context = {}

    article = get_object_or_404(Blog, slug=slug)

    context['article'] = article
    context['related_articles'] = Blog.objects.filter(category=article.category).exclude(id=article.pk)
    context['categories'] = BlogCategory.objects.all()

    return render(request, 'blog_page.html', context)


def send_contact(request):
    context = {}

    context['contact_form'] = AskForFormCaptcha()
    contact_form = AskForFormCaptcha(request.POST or None)
    if request.POST:

        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            subject = request.POST.get("subject", "")
            message = request.POST.get("message", "")

            SiteContact.objects.create(name=name, email=email, subject=subject, message=message)

            return HttpResponse('OK')

        return HttpResponse('ERROR')

    return HttpResponse('ERROR')