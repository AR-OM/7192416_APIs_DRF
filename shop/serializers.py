from rest_framework import serializers

from .models import Category, Product, Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'name', 'date_created', 'date_updated', 'price', 'product']


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'date_created', 'date_updated', 'category']


class ProductDetailSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'date_created', 'date_updated', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated']


class CategoryDetailSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated',  'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductListSerializer(queryset, many=True)
        return serializer.data

