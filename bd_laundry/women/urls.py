from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.women, name='women')
]
