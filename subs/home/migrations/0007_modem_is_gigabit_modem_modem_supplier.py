# Generated by Django 5.1.4 on 2025-01-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_modem_created_on_modem_updated_on_plan_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modem',
            name='is_gigabit',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='modem',
            name='modem_supplier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
