from django.conf.urls import url, include
from . import views # '.' - importing from a current package

urlpatterns = [
    url(r'^contact/', views.contact, name='contact'),
    url(r'^$', views.index, name='index'), #returns whatever is in index function in views.py
]