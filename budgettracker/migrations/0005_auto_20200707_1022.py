# Generated by Django 3.0.5 on 2020-07-07 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgettracker', '0004_budgetleft'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgettracker',
            options={'ordering': ['category']},
        ),
    ]
