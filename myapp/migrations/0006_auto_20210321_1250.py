# Generated by Django 3.1.4 on 2021-03-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note_updated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.FileField(upload_to='post-img')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='notes',
            name='field_name',
        ),
    ]
