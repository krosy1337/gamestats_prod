# Generated by Django 3.1.4 on 2021-01-26 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210115_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverwatchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.CharField(default=None, max_length=200, null=True)),
                ('result', models.BooleanField(default=False)),
                ('result_num', models.BigIntegerField(default=None, null=True)),
                ('result_str', models.CharField(default=None, max_length=250, null=True)),
                ('result_big_str', models.CharField(default=None, max_length=1000, null=True)),
                ('result_json', models.CharField(default=None, max_length=5000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='csresult',
            name='result_big_str',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='csresult',
            name='result_json',
            field=models.CharField(default=None, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='csresult',
            name='result_num',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='csresult',
            name='result_str',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='dotaresult',
            name='result_big_str',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dotaresult',
            name='result_json',
            field=models.CharField(default=None, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='dotaresult',
            name='result_num',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='dotaresult',
            name='result_str',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='talantuser',
            name='overwatch_task',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='csresult',
            name='result',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dotaresult',
            name='result',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talantuser',
            name='overwatch_result',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.overwatchresult'),
        ),
    ]
