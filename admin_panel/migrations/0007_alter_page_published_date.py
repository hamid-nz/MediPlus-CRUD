# Generated by Django 5.0 on 2024-02-06 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_alter_page_published_date_alter_topcard_discription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 10, 22, 8, 862346, tzinfo=datetime.timezone.utc)),
        ),
    ]
