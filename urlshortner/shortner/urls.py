from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shortner-home'),
    path('shortner/<str:short_url>', views.show, name='url-show')
]