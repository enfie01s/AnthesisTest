from django.conf.urls import url
from . import views

app_name='question3'

urlpatterns = [
    url(r'^(?P[\d\w-]+)$', views.farm, name='farm'),
]