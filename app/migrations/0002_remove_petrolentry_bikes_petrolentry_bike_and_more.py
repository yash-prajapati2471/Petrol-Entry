# Generated by Django 5.2 on 2025-05-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petrolentry',
            name='bikes',
        ),
        migrations.AddField(
            model_name='petrolentry',
            name='bike',
            field=models.CharField(choices=[('platina', 'Platina'), ('splendor', 'Splendor')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Bike',
        ),
    ]
