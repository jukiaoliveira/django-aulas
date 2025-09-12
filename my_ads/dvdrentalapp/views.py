#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Customer, Category, Rental, Payment, Address, Film, Language, Country
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from django.utils import timezone

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
    myAddress = Address.objects.filter(customer__customer_id=id)

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
        return redirect(f'/address/{address.customer.id}')
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

def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')

        category1 = Category(name=name, last_update=timezone.now())
        category1.save()

        return redirect('/category1')

    return render(request, 'add_category.html')

def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.last_update = datetime.now()
        category.save()
        return redirect('/category1')
    return render(request, 'edit_category.html', {'category' : category})

def list_filme(request):
    films = Film.objects.all()
    return render(request, 'list_filme.html', {'films':films})

def add_film(request):
    if request.method == "POST":
        name = request.POST.get('name')

        if name:
            film = Film(title=name, language_id=1, rental_duration=3, rental_rate=4.99, replacement_cost=19.99, last_update=timezone.now())
            film.save()
            return redirect('/film')
        else:
            return render(request, 'add_film.html', {'error': 'O nome do filme é obrigatório.'})

    return render(request, 'add_film.html')

# def listacustomer(request):
#     mycustomers = Customer.objects.all().values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name__contains='Karen').values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(last_name__icontains='mill').values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name__endswith='s').values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name__iendswith='s').values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name__exact='Phyllis').values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name__iexact='phyllis').values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name__in=['Phyllis', 'Dennis', 'Nicholas']).values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(customer_id__gt=500).values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(customer_id__gte=500).values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(customer_id__lt=15).values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(customer_id__lte=15).values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# # def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name = 'Maria', customer_id=7).values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# def listacustomer(request):
#     mycustomers = Customer.objects.filter(first_name = 'Maria').values() | Customer.objects.filter(customer_id=8).values()
#     template = loader.get_template('customers.html')
#     context = {
#         'listcustomer':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

# def listacustomer1(request):
#     search_name = request.GET.get('search_name', '')

#     if search_name:
#         mycustomers = Customer.objects.filter(first_name__contains=search_name).values()
#     else:
#         mycustomers = Customer.objects.all().values()

#     template = loader.get_template('customers1.html')
#     context = {
#         'listcustomer1':mycustomers,
#     }
#     return HttpResponse(template.render(context, request))

def listacountry(request):
    search_name = request.GET.get('search_name', '')

    if search_name:
        mycountry = Country.objects.filter(country__contains=search_name).values() | Country.objects.filter(country_id__contains=search_name).values()
    else:
        mycountry = Country.objects.all().values()

    template = loader.get_template('country.html')
    context = {
        'listcountry':mycountry,
    }
    return HttpResponse(template.render(context, request))

def listacustomer2(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('customers2.html')
    context = {
        'listcustomer2': mycustomers,
    }
    return HttpResponse(template.render(context, request))