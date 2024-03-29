# Generated by Django 3.2.5 on 2021-07-18 09:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shareholder', '0002_remove_shareholder_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shareholder',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', help_text='Mobile Number', max_length=128, region=None, verbose_name='Mobile Number'),
            preserve_default=False,
        ),
    ]
