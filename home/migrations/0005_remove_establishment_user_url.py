# Generated by Django 4.2.6 on 2023-11-25 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_establishment_account_establishment_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishment',
            name='user_url',
        ),
    ]
