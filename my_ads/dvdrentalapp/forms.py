from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        #fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'address', 'activebool', 'store_id', 'create_date']