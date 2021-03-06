# Generated by Django 2.2.4 on 2019-09-30 11:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20190926_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='TownshipPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=None, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('mode', models.IntegerField(blank=True, default=None, null=True)),
                ('paytm_order_id', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('paytm_checksumhash', models.CharField(blank=True, default=None, max_length=108, null=True)),
                ('township', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Township')),
            ],
        ),
    ]
