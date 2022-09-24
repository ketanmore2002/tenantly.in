# Generated by Django 4.1.1 on 2022-09-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_paytm_auth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paytm_auth',
            name='text',
        ),
        migrations.RemoveField(
            model_name='paytm_auth',
            name='url',
        ),
        migrations.AddField(
            model_name='paytm_auth',
            name='MERCHANT_ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paytm_auth',
            name='MERCHANT_KEY',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]