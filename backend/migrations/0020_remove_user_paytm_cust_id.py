# Generated by Django 2.2.4 on 2019-09-30 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_auto_20190930_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='paytm_cust_id',
        ),
    ]
