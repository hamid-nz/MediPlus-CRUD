# Generated by Django 5.0 on 2024-02-06 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0014_appointment_alter_page_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='page',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 23, 22, 55, 235359, tzinfo=datetime.timezone.utc)),
        ),
    ]