# Generated by Django 4.0.3 on 2022-03-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_rename_auction_listing_auctionlisting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
