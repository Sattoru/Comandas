# Generated by Django 4.0.4 on 2022-04-22 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='nome',
            new_name='pedido',
        ),
    ]
