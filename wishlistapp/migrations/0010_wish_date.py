# Generated by Django 2.1.5 on 2020-02-20 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wishlistapp', '0009_auto_20200220_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]