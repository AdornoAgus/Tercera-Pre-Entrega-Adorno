# Generated by Django 4.1.6 on 2023-02-16 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_buloneria', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clientes_1',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='deposito_1',
            new_name='Deposito',
        ),
        migrations.RenameModel(
            old_name='proveedor_1',
            new_name='Proveedor',
        ),
    ]
