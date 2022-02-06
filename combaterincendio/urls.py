
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import IndexView
from combaterincendio import views as combaterincendio_views
from django.urls import path
from combaterincendio import settings
from combaterincendio import views

admin.autodiscover()
admin.site.site_header = u'Combater Incêndio - Back office '
admin.site.index_title = u'Combater Incêndio - Administração'
admin.site.site_title = u'Combater Incêndio - Back office'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('blog/', combaterincendio_views.blog, name='blog'),
    path('blog/<slug:slug>/', combaterincendio_views.blog_page, name='blog_page'),
    path('enviar-contato/', combaterincendio_views.send_contact, name='send_contact'),


    path('tinymce/', include('tinymce.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [url(r'^media/(?P<path>.)$', serve, {'document_root': settings.MEDIA_ROOT, }),
                url(r'^static/(?P<path>.)$', serve, {'document_root': settings.STATIC_ROOT}), ]
