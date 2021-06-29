# Generated by Django 3.2.4 on 2021-06-18 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('business', '0006_alter_barangay_barangay_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team_business', to='team.team'),
            preserve_default=False,
        ),
    ]