from django.db import models

class Configuration(models.Model):
    ops_name = models.CharField(max_length=200)
    ops_tel = models.IntegerField()
    supplier_name = models.CharField(max_length=200,null=True)
    supplier_tel = models.IntegerField(null=True)
    device_factory = models.CharField(max_length=200)
    device_location = models.CharField(max_length=200)
    device_name = models.CharField(max_length=200)
    device_ip = models.IntegerField()
    applicant_name = models.CharField(max_length=200)
    device_add = models.CharField(max_length=200)
    application_date = models.DateTimeField()
    end_date = models.DateTimeField()
    change_scope = models.CharField(max_length=800)
    change_content = models.CharField(max_length=800)
    test_method = models.CharField(max_length=800)
    change_summary = models.CharField(max_length=800)
