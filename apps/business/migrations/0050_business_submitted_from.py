# Generated by Django 3.2.4 on 2021-07-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0049_business_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='submitted_from',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
