# Generated by Django 2.2.5 on 2019-09-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryAlgorithmPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('algorithm', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmailLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailAddress', models.EmailField(max_length=100, unique=True)),
                ('emailPass', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('categoryAlgorithmPair', models.ManyToManyField(to='src.CategoryAlgorithmPair')),
                ('emailLogins', models.ManyToManyField(to='src.EmailLogin')),
            ],
        ),
    ]
