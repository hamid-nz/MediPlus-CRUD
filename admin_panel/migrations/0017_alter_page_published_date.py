# Generated by Django 5.0 on 2024-02-08 03:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0016_homepagecontent_batch_2_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 3, 4, 39, 562703, tzinfo=datetime.timezone.utc)),
        ),
    ]