# Generated by Django 4.1.1 on 2022-09-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_paytm_auth_text_remove_paytm_auth_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement_orders',
            name='total_amount',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
