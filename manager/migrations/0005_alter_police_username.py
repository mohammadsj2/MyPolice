# Generated by Django 3.2.9 on 2021-11-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20211114_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]