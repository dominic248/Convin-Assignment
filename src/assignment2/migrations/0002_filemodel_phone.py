# Generated by Django 3.0 on 2019-12-15 15:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='9594183245', max_length=128, region=None),
            preserve_default=False,
        ),
    ]