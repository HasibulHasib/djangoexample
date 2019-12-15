
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.order,name='order'),
    path('order_list/', views.order_list, name='order_list'),
    # path(r'^order_list/$', views.order, name='order_list'),

]
