from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username', 'password', 'role')
        # this makes the password unvisible in response so it is always safe
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
