# Generated by Django 3.2.5 on 2021-07-18 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareholder', '0005_auto_20210718_1249'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Installments',
            new_name='Installment',
        ),
    ]
