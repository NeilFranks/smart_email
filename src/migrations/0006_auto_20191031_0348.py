# Generated by Django 2.2.6 on 2019-10-31 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('src', '0005_auto_20191025_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailToken',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('emailToken', models.TextField()),
                ('address', models.TextField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='emailToken', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='EmailPass',
        ),
    ]
