from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from weather import views

urlpatterns = [
    url(r'^weather/$',
        login_required(views.weather), name='weather'),
]
