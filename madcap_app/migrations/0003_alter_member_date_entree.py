# Generated by Django 5.1.4 on 2024-12-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madcap_app', '0002_member_date_entree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_entree',
            field=models.DateField(blank=True, null=True),
        ),
    ]
