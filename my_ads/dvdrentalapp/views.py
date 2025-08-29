#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Customer, Category, Rental, Payment
from django.shortcuts import get_object_or_404

def customer(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'mycustomer': mycustomers,
}

    return HttpResponse(template.render(context, request))

def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)

    template = loader.get_template('detalhes.html')
    context = {
        'myDetalhe' : myDetalhes,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

def pagamentos(request, id):
    myPayment = Payment.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)

    template = loader.get_template('pagamentos.html')
    context = {
        'myPayment' : myPayment,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

def category(request):
    category = Category.objects.all().values()
    template = loader.get_template('all_categories.html')
    context = {
        'category': category,
}

    return HttpResponse(template.render(context, request))