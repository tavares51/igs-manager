from os import read
from rest_framework import serializers
from .models import Employee, Departament


class DepartamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departament
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    #departament = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'departament']
        #depth = 1


