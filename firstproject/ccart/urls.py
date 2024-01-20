from django.urls import path
from . import views 

urlpatterns = [
    path('', views.cart , name='cart'),
    path('checkout', views.checkout , name='checkout'),
    path('confirmation', views.confirmation , name='confirmation'),

]

