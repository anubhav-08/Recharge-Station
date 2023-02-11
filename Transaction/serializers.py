from rest_framework import serializers

from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {
            'user': {'write_only': True},
        }

    def create(self, validated_data):
        transaction = Transaction.objects.create(**validated_data)
        return transaction