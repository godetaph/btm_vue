# Generated by Django 3.2.4 on 2021-06-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_alter_business_is_business_permit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='is_notice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
