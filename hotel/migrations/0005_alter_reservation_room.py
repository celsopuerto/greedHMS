# Generated by Django 4.2 on 2024-01-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_reservation_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.CharField(max_length=100),
        ),
    ]
