# Generated by Django 3.2.10 on 2021-12-12 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_offer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='landtype',
            options={'ordering': ['-property_type']},
        ),
    ]
