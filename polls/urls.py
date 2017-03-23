from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base$', views.base, name='base'),
    url(r'^academic$', views.academic, name='academic'),
    url(r'^additional$', views.additional, name='additional'),
    url(r'^success$', views.success, name='success'),
    url(r'^tpobasic$', views.tpobasic, name='tpobasic'),
]
