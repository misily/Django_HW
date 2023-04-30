from rest_framework import serializers
from user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self,obj, validated_data):
        user = super().create(obj, validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ("email", "gender", "age", "introduction", "name")


