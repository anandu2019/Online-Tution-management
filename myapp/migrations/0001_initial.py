# Generated by Django 3.1.4 on 2021-03-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ph_number', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
