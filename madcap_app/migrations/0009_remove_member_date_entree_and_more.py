# Generated by Django 5.1.5 on 2025-03-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madcap_app', '0008_merge_20250317_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='date_entree',
        ),
        migrations.AlterField(
            model_name='member',
            name='annee_adhesion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
