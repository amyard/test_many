from django.urls import path

from gen import views


app_name = 'gen'

urlpatterns = [
    path('', views.index, name='base_view'),
]