# Generated by Django 3.0.5 on 2020-05-01 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200430_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountbalance',
            old_name='account_name',
            new_name='name',
        ),
    ]
