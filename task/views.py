from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Configuration
import json
from django.core import serializers
from datetime import datetime, date


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):

        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)


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
    result = json.dumps(result, cls=JsonCustomEncoder)
    return HttpResponse(result, content_type="application/json")

@csrf_exempt
def task_post(request):
    if request.is_ajax():
        data = request.POST
        print(data)
        return HttpResponse('success')
