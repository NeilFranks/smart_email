# Generated by Django 2.2.7 on 2019-11-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0012_category_label_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='label_id',
            field=models.TextField(),
        ),
    ]
