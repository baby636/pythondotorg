# Generated by Django 2.0.13 on 2021-06-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0026_auto_20210416_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorbenefit',
            name='program_name',
            field=models.CharField(default='Deleted Program', help_text='For display in the contract and sponsor dashboard.', max_length=1024, verbose_name='Program Name'),
            preserve_default=False,
        ),
    ]
