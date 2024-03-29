# Generated by Django 3.2.5 on 2021-07-18 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shareholder', '0004_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='installment_type',
            field=models.IntegerField(choices=[(12, 'Monthly'), (4, 'Quarterly'), (1, 'Annual')]),
        ),
        migrations.AlterField(
            model_name='share',
            name='shareholder',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shareholder.shareholder'),
        ),
        migrations.CreateModel(
            name='Installments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareholder.share')),
            ],
        ),
    ]
