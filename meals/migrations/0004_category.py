# Generated by Django 3.2 on 2021-04-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20210424_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
