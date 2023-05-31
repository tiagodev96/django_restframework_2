# Generated by Django 4.2.1 on 2023-05-31 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('document', models.CharField(max_length=11, unique=True)),
                ('phone', models.CharField(max_length=14)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
