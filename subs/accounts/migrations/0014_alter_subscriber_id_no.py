# Generated by Django 5.1.4 on 2025-01-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_subscriber_id_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='id_no',
            field=models.CharField(editable=False, max_length=20, unique=True),
        ),
    ]
