# Generated by Django 3.1.2 on 2020-11-01 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('address', models.TextField()),
                ('zip_code', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('price', models.FloatField()),
                ('barcode', models.IntegerField()),
                ('stock', models.IntegerField(default=0)),
                ('seuil', models.IntegerField(default=0)),
                ('is_sold_with_weight', models.BooleanField()),
                ('provider', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.provider')),
            ],
        ),
    ]