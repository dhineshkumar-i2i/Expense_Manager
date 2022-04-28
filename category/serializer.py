from rest_framework import serializers

from category import models


class CategorySerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                           read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                           read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'
