# Generated by Django 5.1.4 on 2025-01-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_subscription_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='purok',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
