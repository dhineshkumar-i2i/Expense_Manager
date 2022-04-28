from rest_framework import serializers

from ledger.serializer import LedgerSerializer
from user import models


class UserSerializer(serializers.ModelSerializer):

    ledger = LedgerSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                           read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                           read_only=True)

    class Meta:
        model = models.UserDetails
        fields = '__all__'
