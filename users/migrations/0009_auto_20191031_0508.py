# Generated by Django 2.2.6 on 2019-10-31 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191031_0353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connectedemail',
            old_name='token',
            new_name='creds',
        ),
    ]
