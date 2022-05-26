from django.forms import ModelForm

from . import models


class OrderForm(ModelForm):
    
    class Meta:
        model = models.Order
        fields = '__all__'



