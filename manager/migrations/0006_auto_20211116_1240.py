# Generated by Django 3.2.9 on 2021-11-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_police_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police',
            name='age',
        ),
        migrations.AddField(
            model_name='police',
            name='birthday',
            field=models.DateField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='message_from_server',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='location',
            field=models.CharField(max_length=40),
        ),
    ]