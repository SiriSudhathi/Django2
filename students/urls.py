from django.conf.urls import url

from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^accounts/profile/$', profile, name='profile'),
    url(r'^student/dashboard/$', student_dashboard, name='student_dashboard'),
    url(r'^student/profile/(?P<pk>\w{0,})/$$', student_profile, name='student_profile'),
    url(r'^student/message/(?P<pk>\w{0,})/$$', student_message, name='student_message'),

    url(r'^faculty/dashboard/$', faculty_dashboard, name='faculty_dashboard'),
    url(r'^tpo/dashboard/$', tpo_dashboard, name='tpo_dashboard'),

    # url(r'^$', views.index, name='index'),
    # url(r'^base$', views.base, name='base'),
    # url(r'^academic$', views.academic, name='academic'),
    # url(r'^additional$', views.additional, name='additional'),
    # url(r'^success$', views.success, name='success'),
]
