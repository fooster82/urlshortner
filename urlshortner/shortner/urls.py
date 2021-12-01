from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shortner-home'),
    path('/shortner/<str:url_shortened>', views.show, name='url-show')
]