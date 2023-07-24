from django.urls import path
from . import views


app_name = 'qr-codes'


urlpatterns = [
    path('', views.qr_home, name='home'),
    path('create/', views.qr_create, name='create')
]
