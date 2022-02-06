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
from django.views.generic import TemplateView
from combaterincendio.models import Servico, DiferencialEsquerdo, DiferencialDireito, Clientes, Blog, BlogCategory, \
    Empresas, SiteContact
from django.http import HttpResponseRedirect, HttpResponse

'''
def index(request):
    context = {}

    if request.POST:
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        if email and password:
            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET.get("next"))
                return HttpResponseRedirect(reverse_lazy('dashboard'))
            else:
                messages.error(request, u"Usuário ou senha incorretos.")
                context['email'] = email

    return render(request, 'index.html', context)
'''


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all
        context['diferencialEsquerdo'] = DiferencialEsquerdo.objects.all
        context['diferencialDireito'] = DiferencialDireito.objects.all
        context['clientes'] = Clientes.objects.all
        context['articles'] = Blog.objects.filter(show_home=True)
        context['empresas'] = Empresas.objects.filter(featured=True)
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
    if request.POST:

        name = request.POST.get("nome", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("assunto", "")
        message = request.POST.get("mensagem", "")

        contact, created = SiteContact.objects.get_or_create(name=name, email=email, subject=subject, message=message)

        if created:
            return HttpResponse("Enviado com sucesso!")

    return HttpResponse("Ocorreu um erro ao enviar as informações, tente novamente")

