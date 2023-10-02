from rest_framework import serializers
from .models import Users, Customer

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username','password','email','phone_number','address','agency']

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['ACCTNO','NO_IDEN','NAMA_NASABAH']