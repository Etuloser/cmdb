from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Configuration
import json
from django.core import serializers
from datetime import datetime, date
from django.contrib.auth.decorators import login_required


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):

        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)

@login_required()
def task(request):
        return render(request, 'task/task.html')


def task_get(request):
    querys = Configuration.objects.all()
    result = ""
    for query in querys:
        tmp = query.__dict__
        del tmp['_state']
        tmp = str(tmp)
        result = result + tmp + ","
    result = eval(result)
    result = { "data":result}
    result = json.dumps(result, cls=JsonCustomEncoder)
    return HttpResponse(result, content_type="application/json")


@csrf_exempt
def task_post(request):
    if request.is_ajax():
        data = request.POST
        c = Configuration(ops_name=data.get('ops_name'), ops_tel=data.get('ops_tel'),
                          supplier_name=data.get('supplier_name'),
                          supplier_tel=data.get('supplier_tel'), device_factory=data.get('device_factory'),
                          device_location=data.get('device_location'),
                          device_name=data.get('device_name'), device_ip=data.get('device_ip'),
                          applicant_name=data.get('applicant_name'),
                          device_add=data.get('device_add'), application_date=data.get('application_date'),
                          end_date=data.get('end_date'), change_scope=data.get('change_scope'),
                          change_content=data.get('change_content'),
                          test_method=data.get('test_method'), change_summary=data.get('change_summary'))
        c.save()
        return HttpResponse('success')
