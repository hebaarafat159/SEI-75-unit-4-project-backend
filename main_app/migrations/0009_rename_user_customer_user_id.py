# Generated by Django 4.2.7 on 2023-11-22 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='user_id',
        ),
    ]
