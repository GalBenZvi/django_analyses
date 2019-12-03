# Generated by Django 2.2.5 on 2019-11-17 03:15

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_analysis', '0010_analysisversion_run_method_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration', django.contrib.postgres.fields.jsonb.JSONField()),
                ('analysis_version', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_analysis.AnalysisVersion')),
            ],
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='inputdefinition',
            name='is_configuration',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='input',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_input_set', to='django_analysis.Run'),
        ),
        migrations.AlterField(
            model_name='output',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_output_set', to='django_analysis.Run'),
        ),
        migrations.CreateModel(
            name='Pipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pipe_destination_set', to='django_analysis.Node')),
                ('destination_port', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_analysis.InputDefinition')),
                ('pipeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_analysis.Pipeline')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pipe_source_set', to='django_analysis.Node')),
                ('source_port', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_analysis.OutputDefinition')),
            ],
        ),
    ]
