# Generated by Django 4.0.6 on 2022-07-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_time_table_scheduleitem_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.DateField(),
        ),
    ]
