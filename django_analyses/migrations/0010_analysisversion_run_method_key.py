# Generated by Django 2.2.5 on 2019-11-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_analysis', '0009_auto_20191114_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisversion',
            name='run_method_key',
            field=models.CharField(default='run', max_length=100),
        ),
    ]
