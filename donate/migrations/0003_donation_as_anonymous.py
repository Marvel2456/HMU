# Generated by Django 4.2.11 on 2024-04-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_alter_donation_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='as_anonymous',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
