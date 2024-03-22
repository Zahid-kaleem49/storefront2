from rest_framework import serializers
from decimal import Decimal

from store.models import Product, Collection


# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


# model serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         model = Product
         fields = ['id', 'title', 'description','inventory', 'price_with_tax', 'price', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    price = serializers.DecimalField(max_digits=9, decimal_places=2, source='unit_price')
    collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=9, decimal_places=2, source='unit_price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     description = serializers.CharField(max_length=255)
#     inventory = serializers.IntegerField()
#     last_update = serializers.DateTimeField()
    # one wayto  add stringrelatedfield and add select_related in views

    # collection = serializers.StringRelatedField()
    # OR
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # OR make collection serilizer class and then add to this class
    # collection = CollectionSerializer()



