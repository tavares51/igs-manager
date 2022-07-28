from django.urls import path
from .views import list_employee

urlpatterns = [
    path('', list_employee, name='list-employee'),

]