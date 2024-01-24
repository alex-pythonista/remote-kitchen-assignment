from rest_framework import serializers

from .models import (
    Restaurant,
    Menu,
    Item
)


class RestaurantCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = [
            "restaurant_name",
            "address",
            "hotline_number"
        ]


class RestaurantUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = [
            "restaurant_name",
            "address",
            "hotline_number",
            "opening_hours",
            "managers"
        ]

    def update(self, instance, validated_data):
        
        instance.restaurant_name = validated_data.get('restaurant_name', instance.restaurant_name)
        instance.address = validated_data.get('address', instance.address)
        instance.hotline_number = validated_data.get('hotline_number', instance.hotline_number)
        instance.opening_hours = validated_data.get('opening_hours', instance.opening_hours)

        if 'managers' in validated_data:
            instance.managers.set(validated_data['managers'])
        instance.save()
        return instance


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.details = validated_data.get('details', instance.details)
        
        instance.save()
        return instance


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"

    def update(self, instance, validated_data):
        
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        
        instance.save()
        return instance
