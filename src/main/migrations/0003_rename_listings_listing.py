# Generated by Django 5.0 on 2023-12-23 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_listings_brand_listings_color_listings_description_and_more'),
        ('users', '0006_alter_profiles_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]
