from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Account


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', 'last_name', 'first_name',
                  'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'last_name': {'required': True},
            'first_name': {'required': True},
            'username': {'required': True}
        }

    def create(self, validated_data):

        password = validated_data.pop('password')

        account_data = validated_data.pop('account', None)

        user = super(UserSerializer, self).create(validated_data)
        account, wasCreated = self.update_or_create_account(user, account_data)
        user.set_password(password)
        user.save()
        account.save()
        return user

    def update(self, instance, validated_data):
        account_data = validated_data.pop('account', None)
        self.update_or_create_account(instance, account_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def update_or_create_account(self, user, account_data):
        return Account.objects.update_or_create(user=user, defaults=account_data)