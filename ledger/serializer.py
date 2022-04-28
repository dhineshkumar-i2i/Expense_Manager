from rest_framework import serializers

from ledger import models


class LedgerSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                           read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S",
                                           read_only=True)

    class Meta:
        model = models.Ledger
        fields = '__all__'
