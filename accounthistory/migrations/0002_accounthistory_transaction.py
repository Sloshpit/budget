# Generated by Django 3.0.5 on 2020-06-04 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20200519_2148'),
        ('accounthistory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounthistory',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transactions.Transaction'),
        ),
    ]
