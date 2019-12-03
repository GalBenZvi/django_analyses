# Generated by Django 2.2.5 on 2019-11-13 03:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_analysis', '0005_auto_20191111_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListInputDefinition',
            fields=[
                ('inputdefinition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_analysis.InputDefinition')),
                ('element_type', models.CharField(choices=[('STR', 'String'), ('INT', 'Integer'), ('FLT', 'Float'), ('BLN', 'Boolean')], max_length=3)),
                ('min_length', models.PositiveIntegerField(blank=True, null=True)),
                ('max_length', models.PositiveIntegerField(blank=True, null=True)),
            ],
            bases=('django_analysis.inputdefinition',),
        ),
        migrations.CreateModel(
            name='OutputDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='run',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='fileinput',
            old_name='path',
            new_name='value',
        ),
        migrations.AddField(
            model_name='booleaninput',
            name='definition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='input_set', to='django_analysis.BooleanInputDefinition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booleaninputdefinition',
            name='default',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analysisversion',
            name='analysis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='version_set', to='django_analysis.Analysis'),
        ),
        migrations.AlterField(
            model_name='fileinput',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='input_set', to='django_analysis.FileInputDefinition'),
        ),
        migrations.AlterField(
            model_name='floatinput',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='input_set', to='django_analysis.FloatInputDefinition'),
        ),
        migrations.AlterField(
            model_name='integerinput',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='input_set', to='django_analysis.IntegerInputDefinition'),
        ),
        migrations.AlterField(
            model_name='stringinput',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='input_set', to='django_analysis.StringInputDefinition'),
        ),
        migrations.CreateModel(
            name='FileOutputDefinition',
            fields=[
                ('outputdefinition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_analysis.OutputDefinition')),
            ],
            bases=('django_analysis.outputdefinition',),
        ),
        migrations.CreateModel(
            name='OutputSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_analysis.Analysis')),
                ('output_definitions', models.ManyToManyField(to='django_analysis.OutputDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_analysis.Run')),
            ],
        ),
        migrations.CreateModel(
            name='ListInput',
            fields=[
                ('input_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_analysis.Input')),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='input_set', to='django_analysis.ListInputDefinition')),
            ],
            bases=('django_analysis.input',),
        ),
        migrations.AddField(
            model_name='analysisversion',
            name='output_specification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='analysis_version_set', to='django_analysis.OutputSpecification'),
        ),
        migrations.CreateModel(
            name='FileOutput',
            fields=[
                ('output_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_analysis.Output')),
                ('value', models.FilePathField(verbose_name='/home/zvi/Projects/pylabber/media')),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='output_set', to='django_analysis.FileOutputDefinition')),
            ],
            bases=('django_analysis.output',),
        ),
    ]
