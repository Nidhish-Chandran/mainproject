# Generated by Django 5.1.4 on 2025-01-30 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0005_logintable_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Expertes', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner.logintable')),
            ],
        ),
    ]
