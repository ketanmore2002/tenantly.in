# Generated by Django 4.1.1 on 2022-09-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_agreement_orders_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement_orders',
            name='total_amount',
            field=models.CharField(blank=True, default='1000', max_length=30, null=True),
        ),
    ]