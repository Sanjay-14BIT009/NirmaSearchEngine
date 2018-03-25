from django.conf.urls import url
from django.urls import include,path
from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),

    url(r'^(?P<que>([\s\S]+))/$', views.Search, name='Search'),
}
