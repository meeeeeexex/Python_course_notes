# Generated by Django 4.0.4 on 2022-05-03 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_alter_excursion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excursionvisiting',
            options={'ordering': ['-user_rate']},
        ),
    ]
