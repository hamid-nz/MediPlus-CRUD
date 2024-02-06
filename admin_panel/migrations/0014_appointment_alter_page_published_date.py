# Generated by Django 5.0 on 2024-02-06 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0013_delete_topcard_homepagecontent_dctor_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('email', models.EmailField(default='', max_length=100, verbose_name='E Mail')),
                ('phone', models.IntegerField(default='', max_length=11, verbose_name='Phone')),
                ('published_date', models.DateTimeField(default='')),
                ('department', models.CharField(choices=[('Dentistry', 'dentistry'), ('Crdiology', 'cardiology'), ('Childrens', 'childrens'), ('Pet Care', 'pet care'), ('OPD', 'opd')], max_length=10)),
                ('message', models.CharField(blank=True, max_length=500, verbose_name='Your Message')),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 23, 8, 11, 105810, tzinfo=datetime.timezone.utc)),
        ),
    ]