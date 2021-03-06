# Generated by Django 4.0.4 on 2022-04-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('city_location', models.CharField(choices=[('London', 'London'), ('Paris', 'Paris'), ('Berlin', 'Berlin'), ('Lisbon', 'Lisbon')], default='not specified', max_length=25)),
                ('rating', models.PositiveIntegerField(blank=True, null=True)),
                ('square', models.PositiveIntegerField()),
                ('amount_of_beds', models.PositiveIntegerField(default=1)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[], default='not specified', max_length=25)),
                ('duration', models.PositiveSmallIntegerField(default=30)),
                ('interests', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.PositiveIntegerField()),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('family_size', models.IntegerField(default=1)),
                ('wealthy_status', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high'), ('not specified', 'not specified')], default='not specified', max_length=25)),
                ('last_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
