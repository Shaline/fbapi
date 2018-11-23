from django.conf import settings

from rest_framework import serializers


def is_digit(value):
    if type(value) != str or not value.isdigit():
        raise serializers.ValidationError('This field must contain only digits')


class UserListJsonSerializer(serializers.Serializer):
    label_id = serializers.CharField()
    users = serializers.ListField(
            child=serializers.CharField(validators=[is_digit]),
            min_length=1,
            max_length=settings.API_MAX_USERS
    )


class UserListCsvSerializer(serializers.Serializer):
    pass
