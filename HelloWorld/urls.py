from django.conf.urls import url

from . import view

urlpatterns = [
    url('hello/', view.hello),
]