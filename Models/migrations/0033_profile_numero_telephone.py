# Generated by Django 4.2.6 on 2024-07-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0032_annonces_email_annonces_vu_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='numero_telephone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]