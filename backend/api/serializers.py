from rest_framework import serializers

from .models import Product, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'created_at', 'updated_at')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'quantity', 'created_at', 'updated_at')
