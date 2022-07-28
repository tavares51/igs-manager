from rest_framework import viewsets
from django.shortcuts import render
from .models import Employee, Departament
from .serializer import EmployeeSerializer, DepartamentSerializer
from rest_framework.response import Response


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'delete']

    def list(self, request):
        response = []
        for e in Employee.objects.all():
            data = {
                'id' : e.pk,
                'name' : e.name,
                'email' : e.email,
                'departament' : e.departament.name
            }
            response.append(data)
        return Response(response)


class DepartamentViewSet(viewsets.ModelViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    http_method_names = ['get', 'post', 'delete']


def list_employee(request, template_name="list-employee.html"):
    employees = Employee.objects.all()
    data = {'employees': employees}
    return render(request, template_name, data)