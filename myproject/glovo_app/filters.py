from .models import Store, Product
from django_filters import filterset

class StoreFilterSet(filterset.FilterSet):
    class Meta:
        model = Store
        fields = {
            'category' : ['exact'],

        }



class ProductFilterSet(filterset.FilterSet):
    class Meta:
        model = Product
        fields = {
            'price' : ['gt', 'lt']
        }