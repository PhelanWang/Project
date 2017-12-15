# coding: utf-8

from rest_framework import serializers
from .models import Category, Entry

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('text', 'date_added')


class EntrySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Entry
        fields = ('name', 'phone_number', 'date_added', 'category')