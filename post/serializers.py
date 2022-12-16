from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializes Person instances"""

    class Meta:
        model = Product
        fields = (
            'name',
        )

    def create(self, validated_data):
        return Product.objects.create(
            user = self.context['request'].user,
            **validated_data
            )