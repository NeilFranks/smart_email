# Generated by Django 2.2.6 on 2019-10-04 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_testobject_testobject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testobject',
            name='name',
        ),
    ]
