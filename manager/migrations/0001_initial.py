# Generated by Django 3.2.9 on 2021-11-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]