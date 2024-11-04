# Generated by Django 5.1.2 on 2024-11-04 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onibus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('capacidade_em_pe', models.IntegerField()),
                ('capacidade_sentados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Linha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rastreamento.rota')),
            ],
        ),
    ]