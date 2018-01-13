# coding: utf-8

from rest_framework import serializers
from .models import Category, Entry
from django.contrib.auth.models import User


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


class UserSerializer(serializers.ModelSerializer):
    # categorys = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'categorys')