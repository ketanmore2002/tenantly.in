# Generated by Django 4.1.1 on 2022-09-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_agreement_orders_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement_orders',
            name='package_type',
            field=models.CharField(blank=True, default='Rental Agreement', max_length=30, null=True),
        ),
    ]