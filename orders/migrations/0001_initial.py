# Generated by Django 4.1.1 on 2022-09-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement_Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('type_of_package', models.CharField(max_length=30)),
                ('agreement_duration', models.CharField(max_length=30)),
                ('agreement_startdate', models.CharField(max_length=30)),
                ('monthly_rent_amount', models.CharField(max_length=30)),
                ('refundable_deposit_amount', models.CharField(max_length=30)),
                ('i_am', models.CharField(max_length=30)),
                ('type_of_property', models.CharField(max_length=30)),
                ('house_number', models.CharField(max_length=30)),
                ('building_number', models.CharField(max_length=30)),
                ('locality', models.CharField(max_length=30)),
                ('number_of_bedrooms', models.CharField(max_length=30)),
                ('number_of_bathrooms', models.CharField(max_length=30)),
                ('road_street', models.CharField(max_length=30)),
                ('property_pincode', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('property_number_type', models.CharField(max_length=30)),
                ('property_number', models.CharField(max_length=30)),
                ('flat_house_bluiltup_area', models.CharField(max_length=30)),
                ('bluit_area_unit', models.CharField(max_length=30)),
                ('property_use', models.CharField(max_length=30)),
                ('gallary_area', models.CharField(max_length=30)),
                ('gallary_area_unit', models.CharField(max_length=30)),
                ('praking_area', models.CharField(max_length=30)),
                ('praking_area_unit', models.CharField(max_length=30)),
                ('landlord_party_entity_type', models.CharField(max_length=30)),
                ('landlord_first_name', models.CharField(max_length=30)),
                ('landlord_middle_name', models.CharField(max_length=30)),
                ('landlord_age', models.CharField(max_length=30)),
                ('landlord_gender', models.CharField(max_length=30)),
                ('landlord_occupation', models.CharField(max_length=30)),
                ('landlord_phone_number', models.CharField(max_length=30)),
                ('landlord_aadhar_number', models.CharField(max_length=30)),
                ('landlord_pan_number', models.CharField(max_length=30)),
                ('landlord_email', models.CharField(max_length=30)),
                ('landlord_build_name', models.CharField(max_length=30)),
                ('landlord_flat_house_number', models.CharField(max_length=30)),
                ('landlord_floor_number', models.CharField(max_length=30)),
                ('landlord_road_street', models.CharField(max_length=30)),
                ('landlord_pincode', models.CharField(max_length=30)),
                ('landlord_village_city', models.CharField(max_length=30)),
                ('landlord_district', models.CharField(max_length=30)),
                ('landlord_state', models.CharField(max_length=30)),
                ('landlord_executing_through', models.CharField(max_length=30)),
                ('tenent_party_entity_type', models.CharField(max_length=30)),
                ('tenent_first_name', models.CharField(max_length=30)),
                ('tenent_middle_name', models.CharField(max_length=30)),
                ('tenent_age', models.CharField(max_length=30)),
                ('tenent_gender', models.CharField(max_length=30)),
                ('tenent_occupation', models.CharField(max_length=30)),
                ('tenent_phone_number', models.CharField(max_length=30)),
                ('tenent_aadhar_number', models.CharField(max_length=30)),
                ('tenent_pan_number', models.CharField(max_length=30)),
                ('tenent_email', models.CharField(max_length=30)),
                ('tenent_build_name', models.CharField(max_length=30)),
                ('tenent_flat_house_number', models.CharField(max_length=30)),
                ('tenent_floor_number', models.CharField(max_length=30)),
                ('tenent_road_street', models.CharField(max_length=30)),
                ('tenent_pincode', models.CharField(max_length=30)),
                ('tenent_village_city', models.CharField(max_length=30)),
                ('tenent_district', models.CharField(max_length=30)),
                ('tenent_state', models.CharField(max_length=30)),
                ('tenent_executing_through', models.CharField(max_length=30)),
                ('non_refundable_amount', models.CharField(max_length=30)),
                ('maintaiance_paid_by', models.CharField(max_length=30)),
                ('minimum_lockin_period', models.CharField(max_length=30)),
                ('notice_period', models.CharField(max_length=30)),
                ('stamp_and_registration_fee_paid_by', models.CharField(max_length=30)),
                ('miscellaneous', models.CharField(max_length=1000)),
            ],
        ),
    ]
