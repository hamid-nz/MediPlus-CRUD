# Generated by Django 5.0 on 2024-02-06 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_alter_page_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Site Title')),
                ('discription', models.CharField(blank=True, max_length=500, verbose_name='Site Discription')),
                ('page_content_1', models.CharField(blank=True, max_length=1000, verbose_name='Content Box 1')),
                ('page_content_2', models.CharField(blank=True, max_length=1000, verbose_name='Content Box 2')),
                ('hospital_rooms', models.CharField(max_length=100, verbose_name='Hospital Rooms')),
                ('specialist_doctors', models.CharField(max_length=100, verbose_name='Specialist Doctors')),
                ('happy_patient', models.CharField(max_length=100, verbose_name='Happy Patients')),
                ('years_of_experience', models.CharField(max_length=100, verbose_name='Years of Experience')),
                ('about_h3', models.CharField(blank=True, max_length=100, verbose_name='3rd Heading')),
                ('about_content', models.CharField(blank=True, max_length=1000, verbose_name='About content')),
                ('emergency_section_h3', models.CharField(blank=True, max_length=100, verbose_name='Emergency section heading')),
                ('emergency_section_content', models.CharField(blank=True, max_length=1000, verbose_name='Emergency section content')),
                ('batch_2_heading', models.CharField(blank=True, max_length=100, verbose_name='batch 2 heading')),
                ('batch_2_price', models.CharField(blank=True, max_length=100, verbose_name='batch 2 price')),
                ('batch_3_content', models.CharField(blank=True, max_length=1000, verbose_name='batch 2 content')),
                ('batch_1_heading', models.CharField(blank=True, max_length=100, verbose_name='batch 3 heading')),
                ('batch_1_price', models.CharField(blank=True, max_length=100, verbose_name='batch 3 price')),
                ('batch_1_content', models.CharField(blank=True, max_length=1000, verbose_name='batch 3 content')),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 12, 23, 5, 249655, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='topcard',
            name='working_day_from',
            field=models.CharField(blank=True, choices=[('Monday', 'Mon'), ('Tuesday', 'Tue'), ('Wednesday', 'Wed'), ('Thursday', 'Thurs'), ('Friday', 'Fri'), ('Saturday', 'Sat'), ('Sunday', 'Sun')], max_length=10),
        ),
        migrations.AlterField(
            model_name='topcard',
            name='working_day_to',
            field=models.CharField(blank=True, choices=[('Monday', 'Mon'), ('Tuesday', 'Tue'), ('Wednesday', 'Wed'), ('Thursday', 'Thurs'), ('Friday', 'Fri'), ('Saturday', 'Sat'), ('Sunday', 'Sun')], max_length=10),
        ),
        migrations.AlterField(
            model_name='topcard',
            name='working_hour_from',
            field=models.CharField(blank=True, choices=[('9:00 AM', '9'), ('10:00 AM', '10'), ('11:00 AM', '11'), ('12:00 AM', '12'), ('1:00 PM', '1'), ('2:00 PM', '2'), ('3:00 PM', '3'), ('4:00 PM', '4'), ('5:00 PM', '5'), ('6:00 PM', '6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='topcard',
            name='working_hour_to',
            field=models.CharField(blank=True, choices=[('9:00 AM', '9'), ('10:00 AM', '10'), ('11:00 AM', '11'), ('12:00 AM', '12'), ('1:00 PM', '1'), ('2:00 PM', '2'), ('3:00 PM', '3'), ('4:00 PM', '4'), ('5:00 PM', '5'), ('6:00 PM', '6')], max_length=10),
        ),
    ]
