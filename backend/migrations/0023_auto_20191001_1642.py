# Generated by Django 2.2.4 on 2019-10-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_auto_20191001_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]