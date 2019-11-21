from rest_framework import serializers
from . import models

# class UserSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = models.User
#         fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['password', 'username', 'comp_id', 'tel']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Company
        fields = ['comp_id', 'comp_name', 'address', 'tel']