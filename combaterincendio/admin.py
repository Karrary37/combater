from django.contrib import admin
from django import forms
from tinymce import TinyMCE
from .models import Servico, Diferencial, Clientes, BlogCategory, Blog, Empresas, SiteContact


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Diferencial)
class DiferencialEsquerdoAdmin(admin.ModelAdmin):
    list_display = ('diferencial', 'icone', 'ativo', 'modificado')


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estrelas', 'ativo', 'modificado')


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class BlogForm(forms.ModelForm):
    description = forms.CharField(label=u'Descrição', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm

    list_display = ('title', 'date', 'author', 'category', 'show_home',)
    search_fields = ('title', 'date', 'author', 'category',)
    prepopulated_fields = {'slug': ('title',)}


class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('name', 'featured', 'order', 'website_link')
    search_fields = ('name', 'featured',)


class SiteContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created')
    search_fields = ('name', 'email',)


admin.site.register(SiteContact, SiteContactAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Empresas, EmpresasAdmin)
