# Generated by Django 3.1 on 2020-08-19 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
import rendez_vous.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heure',
            fields=[
                ('heure', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rdv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(blank=True, max_length=150)),
                ('date', models.DateField(default=datetime.date.today, validators=[rendez_vous.models.Rdv.validate_date])),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('heure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rendez_vous.heure')),
            ],
            options={
                'verbose_name': 'Rendez-vous',
                'verbose_name_plural': 'Rendez-vous',
            },
        ),
    ]