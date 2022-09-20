from rest_framework import serializers
from account.models import Account

class AccountSerializer(serializers.Serializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'email']
