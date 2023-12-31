# Generated by Django 3.2 on 2022-12-15 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devon', '0003_janrlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='JanrMisraSoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=150)),
                ('janr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devon.janrlar')),
            ],
            options={
                'verbose_name': 'Janr sozi',
                'verbose_name_plural': 'Janr sozlari',
            },
        ),
        migrations.CreateModel(
            name='JanrMisra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('misra', models.CharField(max_length=300)),
                ('janr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devon.janrlar')),
            ],
            options={
                'verbose_name': 'Janr misrasi',
                'verbose_name_plural': 'Janr misralari',
            },
        ),
    ]
