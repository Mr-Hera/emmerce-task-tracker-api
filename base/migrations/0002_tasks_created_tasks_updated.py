# Generated by Django 4.1.7 on 2023-03-14 22:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
