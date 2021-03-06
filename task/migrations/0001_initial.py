# Generated by Django 2.0.1 on 2018-01-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ops_name', models.CharField(max_length=200)),
                ('ops_tel', models.IntegerField(max_length=200)),
                ('supplier_name', models.CharField(max_length=200)),
                ('supplier_tel', models.IntegerField(max_length=200)),
                ('device_factory', models.CharField(max_length=200)),
                ('device_location', models.CharField(max_length=200)),
                ('device_name', models.CharField(max_length=200)),
                ('device_ip', models.IntegerField(max_length=200)),
                ('applicant_name', models.CharField(max_length=200)),
                ('device_add', models.CharField(max_length=200)),
                ('application_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('change_scope', models.CharField(max_length=800)),
                ('change_content', models.CharField(max_length=800)),
                ('test_method', models.CharField(max_length=800)),
                ('change_summary', models.CharField(max_length=800)),
            ],
        ),
    ]
