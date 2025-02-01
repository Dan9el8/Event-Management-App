from rest_framework import serializers
from .models import User, Event, Registration, Wishlist, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "role"]


class EventSerializer(serializers.ModelSerializer):
    organizer_name = serializers.ReadOnlyField(source="organizer.username")

    class Meta:
        model = Event
        fields = [
            "id", "title", "description", "date", "location", "capacity",
            "category", "image", "organizer", "organizer_name", "created_at", "updated_at",
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ["id", "user", "event", "registered_at"]


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ["id", "user", "event", "added_at"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]
