# Generated by Django 5.1.5 on 2025-02-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='phonenumber',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
