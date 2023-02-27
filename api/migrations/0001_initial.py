# Generated by Django 4.1.7 on 2023-02-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=500, unique=True)),
                ('os', models.CharField(max_length=20)),
            ],
        ),
    ]