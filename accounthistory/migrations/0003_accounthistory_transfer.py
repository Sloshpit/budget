# Generated by Django 3.0.5 on 2020-06-04 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0006_auto_20200604_0709'),
        ('accounthistory', '0002_accounthistory_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounthistory',
            name='transfer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfers.Transfer'),
        ),
    ]