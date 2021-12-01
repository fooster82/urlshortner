from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shortner-home'),
    path('shrinker/<str:short_url>', views.show, name='url-show')
]