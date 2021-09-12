# Generated by Django 3.2.7 on 2021-09-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210611_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizacjevna',
            name='hamowanie',
            field=models.CharField(choices=[('M', 'Magnesy'), ('B', 'Blachy'), ('R', 'RFID'), ('O', 'Optyczne'), ('-', 'Brak')], max_length=1),
        ),
        migrations.AlterField(
            model_name='realizacjevna',
            name='prowadzenie',
            field=models.CharField(choices=[('S', 'Mechaniczno-Indukcyjne'), ('M', 'Mechaniczne'), ('I', 'Indukcyjne'), ('N', 'Swobodnie prowadzone')], max_length=1),
        ),
    ]
