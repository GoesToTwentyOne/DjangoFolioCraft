# Generated by Django 4.2.4 on 2023-09-23 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_provide', '0003_alter_serviceappmodelpart_bullet_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceappmodelpart',
            name='bullet_class',
        ),
    ]
