# Generated by Django 2.2.5 on 2020-03-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20200307_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='api_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
