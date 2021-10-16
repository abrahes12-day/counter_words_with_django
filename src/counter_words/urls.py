from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.counter, name='counter'),
    path('output_counter', views.output_counter, name='output_counter')
]