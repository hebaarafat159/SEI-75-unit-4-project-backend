# Generated by Django 4.2.7 on 2023-11-23 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('avatar_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=250)),
                ('published_date', models.DateField(verbose_name='Published Date')),
                ('cover_image', models.CharField(default='', max_length=225)),
                ('status', models.CharField(choices=[('A', 'Available'), ('B', 'Borrowed')], default='A', max_length=1)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('is_cover', models.BooleanField(default=False)),
                ('Book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.book')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Accepted'), ('P', 'Pending'), ('R', 'Rejected')], default='A', max_length=1)),
                ('customer', models.ForeignKey(default=41, on_delete=django.db.models.deletion.CASCADE, to='main_app.customer')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_requests',
            field=models.ManyToManyField(to='main_app.bookrequest'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(default=41, on_delete=django.db.models.deletion.CASCADE, to='main_app.customer'),
        ),
    ]
