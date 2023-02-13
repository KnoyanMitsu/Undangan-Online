from django.conf.urls import url
from toys import view
from django.urls import path

urlpatterns = [
    url(r'^toys/$', view.toy_list),
    url(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail),
]
