# Generated by Django 3.2 on 2022-12-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gazal', '0011_auto_20221113_1418'),
        ('Devon', '0005_janrmisrasoz_mano'),
    ]

    operations = [
        migrations.AddField(
            model_name='janrmisrasoz',
            name='auditoriya_yoshi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gazal.auditoriya_yoshi'),
        ),
    ]
