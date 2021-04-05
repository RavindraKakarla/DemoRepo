from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse


class EmployeeDetailCBV(View):
     def get(self, request, id, *args, **kwargs):
         emp = Employee.objects.get(id=id)
         emp_data = {'eno': "1", 'ename': "asdf", 'esal': "20.2", 'eaddr': "emp.eaddr"}
         json_data = json.dumps(emp_data)
         return HttpResponse(json_data, content_type='application/json')
