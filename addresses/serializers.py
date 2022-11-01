from rest_framework import serializers

from addresses.models import Address

class AddressesSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Address
        fields = [
            'id',
            'zipcode',
            'district',
            'state',
            'street',
            'number',
        ]
       