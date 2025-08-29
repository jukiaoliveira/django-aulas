from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name='mycustomer'),
    path('detalhes/<int:id>', views.detalhes, name='myDetalhe'),
    path('pagamentos/<int:id>', views.pagamentos, name='myPayment'),
    path('category/', views.category, name='category'),
]
