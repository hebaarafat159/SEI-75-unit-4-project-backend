# Generated by Django 4.2.7 on 2023-11-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]
