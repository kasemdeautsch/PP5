# Generated by Django 4.2.20 on 2025-04-02 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ram',
        ),
    ]
