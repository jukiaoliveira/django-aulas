from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name='mycustomer'),
    path('address/<int:id>', views.address, name='myaddress'),
    path('edit_address/<int:address_id>', views.edit_address, name='edit_address'),
    path('customer1/', views.customer1, name='customer1'),
    path('detalhes/<int:id>', views.detalhes, name='myDetalhe'),
    path('edit_customer/<int:customer_id>', views.edit_customer, name='edit_customer'),
    path('pagamentos/<int:id>', views.pagamentos, name='myPayment'),
    path('category/', views.category, name='category'),
    path('category1/', views.category1, name='category1'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
]
