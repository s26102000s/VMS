# Generated by Django 3.2.2 on 2021-06-09 14:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import visit.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('id_name', models.CharField(max_length=150)),
                ('id_num', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150, unique=True)),
                ('address', models.CharField(max_length=150)),
                ('role', models.CharField(choices=[('HR', 'HR'), ('Security', 'Security')], max_length=20)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('contact', models.PositiveIntegerField(null=True)),
                ('email', models.EmailField(max_length=150, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('college', models.CharField(max_length=250, null=True)),
                ('photo', models.ImageField(null=True, upload_to=visit.validators.content_file_name, validators=[visit.validators.validate_file_extension])),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('from_time', models.TimeField(default=datetime.datetime(2021, 6, 9, 19, 46, 3, 945879))),
                ('to_time', models.TimeField()),
                ('purpose', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('student_entry_time', models.TimeField(blank=True, default=None, null=True)),
                ('student_exit_time', models.TimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='visit.student')),
            ],
            options={
                'permissions': (('is_Security', 'Can edit the entry time of a student or employee'),),
            },
        ),
        migrations.CreateModel(
            name='HR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('is_hr', 'Can edit the meeting time of a visitor'),),
            },
        ),
    ]
