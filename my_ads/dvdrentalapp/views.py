#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Customer, Category

def customer(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'mycustomer': mycustomers,
}

    return HttpResponse(template.render(context, request))

def category(request):
    category = Category.objects.all().values()
    template = loader.get_template('all_categories.html')
    context = {
        'category': category,
}

    return HttpResponse(template.render(context, request))