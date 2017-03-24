from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^frontpage/$', views.next, name='frontpage'),
    url(r'^success/$', views.success, name='success'),
    url(r'^display/$', views.display, name='display'),
]
