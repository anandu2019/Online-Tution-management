# Generated by Django 3.1.4 on 2021-03-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='marksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maths', models.CharField(max_length=10)),
                ('English', models.CharField(max_length=10)),
                ('GK', models.CharField(max_length=10)),
            ],
        ),
    ]
