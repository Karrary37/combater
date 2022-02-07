from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_delete
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.dispatch import receiver
import uuid
from django.utils.translation import gettext_lazy as _


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile."""

        if not email:
            raise ValueError('O e-mail é obrigatório')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a "user profile" inside out system. Stores all user account
    related data, such as 'email address' and 'name'.
    """
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, verbose_name='Telefone', null=True, blank=True, )
    email = models.EmailField(max_length=255, blank=True, unique=True)

    postal_code = models.CharField(max_length=12, verbose_name='CEP', null=True, blank=True, )
    address = models.CharField(max_length=200, verbose_name=u'Endereço', null=True, blank=True, )
    address_neighborhood = models.CharField(max_length=50, verbose_name=u'Bairro', null=True, blank=True, )
    address_number = models.CharField(max_length=50, verbose_name=u'Número', null=True, blank=True, )
    address_complement = models.CharField(max_length=50, verbose_name=u'Complemento', null=True, blank=True, )
    city = models.CharField(max_length=40, verbose_name='Cidade', null=True, blank=True, )
    state = models.CharField(max_length=2, verbose_name='Estado', null=True, blank=True, )

    # child_age = models.SmallIntegerField(verbose_name='Idade do filho(a)', null=True, blank=True, default=None)

    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')

    objects = UserProfileManager()

    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    @property
    def get_full_address(self):
        if self.address_complement:
            return "{0}, {1}, {2}, {3}, {4}, {5} - {6}".format(self.address, self.address_number,
                                                               self.address_complement, self.address_neighborhood,
                                                               self.postal_code, self.city, self.state)
        else:
            return "{0}, {1}, {2}, {3}, {4} - {5}".format(self.address, self.address_number, self.address_neighborhood,
                                                          self.postal_code, self.city, self.state)

    @property
    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return "%s %s" % (self.name, self.name)

    def get_short_name(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.name

    class Meta:
        verbose_name = u"Usuário"
        verbose_name_plural = u"Usuários"
        ordering = ('name',)


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Computador'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Pilha'),
    )
    servico = models.CharField('Seviços', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Diferencial(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Computador'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Pilha'),
    )
    diferencial = models.CharField('Diferencial', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)
    order = models.SmallIntegerField(verbose_name='Ordem', default=0)

    class Meta:
        verbose_name = 'Diferencial '
        verbose_name_plural = 'Diferencial '
        ordering = ("order",)

    def __str__(self):
        return self.diferencial


class Clientes(Base):
    ICONE_CHOICES = (
        ('<span><i class="lni-star-filled"></i></span> </span> <span><i class="lni-star-half"></i></span>'
         '<span><i class="lni-star-half"></i></span> <span><i class="lni-star-half"></i></span>'
         '<span><i class="lni-star-half"></i></span>', 'Uma Estrela'),
        ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> '
         '<span><i class="lni-star-half"></i> </span> <span><i class="lni-star-half"></i></span> <span><i '
         'class="lni-star-half"></i></span>', 'Duas Estrelas'),
        ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i '
         'class="lni-star-filled"></i></span> <span><i class="lni-star-half"></i></span> <span><i '
         'class="lni-star-half"></i></span>', 'Três Estrela'),
        ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i '
         'class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i '
         'class="lni-star-half"></i></span>', 'Quatro Estrela'),
        ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i '
         'class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> '
         '<span><i class="lni-star-filled"></i></span>', 'Cinco Estrela'),
    )
    nome = models.CharField('Nome', max_length=100)
    empresa = models.CharField('Empresa', max_length=100)
    comentario = models.TextField('Comentario', max_length=200)
    estrelas = models.CharField('Estrelas', max_length=250, choices=ICONE_CHOICES)
    imagem = models.ImageField('Foto', upload_to='clientes')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class BlogCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Categoria - Blog'
        verbose_name_plural = u'Categorias - Blog'
        ordering = ('title',)


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    slug = models.SlugField()
    description = models.TextField(verbose_name='Texto')
    image = models.ImageField(upload_to='blog_images', verbose_name='Imagem')
    date = models.DateField(verbose_name='Data')
    category = models.ForeignKey(BlogCategory, verbose_name='Categoria', on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=100, verbose_name='Autor')
    show_home = models.BooleanField(default=False, verbose_name='Mostrar na Home')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Blog'
        verbose_name_plural = u'Blog'


class Empresas(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    logo = models.ImageField(upload_to='clients', verbose_name='Logo', null=True, blank=True)
    featured = models.BooleanField(default=False, verbose_name='Destaque')
    order = models.SmallIntegerField(default=0, verbose_name='Ordem')
    website_link = models.URLField(default=None, null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Empresa"
        verbose_name_plural = u"Empresas"
        ordering = ("order",)


class SiteContact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome', null=True, blank=True)
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    subject = models.CharField(max_length=100, verbose_name='Assunto', null=True, blank=True)
    message = models.TextField(max_length=100, verbose_name='Mensagem', null=True, blank=True)
    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = u"Site - Contato"
        verbose_name_plural = u"Site - Contatos"
        ordering = ('-created',)
