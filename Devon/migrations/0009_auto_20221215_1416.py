# Generated by Django 3.2 on 2022-12-15 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devon', '0008_janrmisrasoz_janr_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChistonJavob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javob', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='janrmisra',
            name='chiston_javobi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Devon.chistonjavob'),
        ),
    ]
