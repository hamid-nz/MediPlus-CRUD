# Generated by Django 5.0 on 2024-02-02 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_alter_page_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='published_date',
        ),
    ]
