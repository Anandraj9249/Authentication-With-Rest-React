from django.db.models import fields
from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email' , 'password' , 'phone']
    def create(self, validated_data):
        user = CustomUser.objects.create(email = validated_data['email'] , phone = validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        return user