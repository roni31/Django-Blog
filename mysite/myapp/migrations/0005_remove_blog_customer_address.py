# Generated by Django 2.2 on 2021-01-25 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_blog_customer_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='customer_address',
        ),
    ]
