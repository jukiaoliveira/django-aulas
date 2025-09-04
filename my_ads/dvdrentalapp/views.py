#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Customer, Category, Rental, Payment, Address
from django.shortcuts import get_object_or_404, render, redirect 
from datetime import datetime

def customer(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'mycustomer': mycustomers,
}

    return HttpResponse(template.render(context, request))

def customer1(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('list_customers.html')
    context = {
        'customer1': mycustomers,
}

    return HttpResponse(template.render(context, request))

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        customer.first_name = request.POST.get('first_name')
        customer.last_name = request.POST.get('last_name')
        customer.email = request.POST.get('email')

        customer.save()
        return redirect('/customer')
    return render(request, 'edit_customer.html', {'customer': customer})

def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)

    template = loader.get_template('detalhes.html')
    context = {
        'myDetalhe' : myDetalhes,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

def address(request, id):
    myAddress = Address.objects.filter(customer__id=id)
    customer = get_object_or_404(Customer, pk=id)

    template = loader.get_template('all_address.html')
    context = {
        'myAddress': myAddress,
        'customer_name': f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))


def edit_address(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    if request.method == "POST":
        address.address2 = request.POST.get('address2')
        address.postal_code = request.POST.get('postal_code')
        address.save()
        return redirect(f'/address/{address_id}')
    return render(request, 'edit_address.html', {'address': address})


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

def category1(request):
    mycategorys = Category.objects.all().values()
    template = loader.get_template('category.html')
    context = {
        'category1': mycategorys,
    }
    return HttpResponse(template.render(context, request))
 
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.last_update = datetime.now()
        category.save()
        return redirect('/category1')
    return render(request, 'edit_category.html', {'category' : category})
 