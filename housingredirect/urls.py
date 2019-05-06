from django.urls import path
from . import views

app_name = 'housingredirect'

urlpatterns = [
    path('', views.about, name='about'),
    path('form/', views.index, name='form'),
]
