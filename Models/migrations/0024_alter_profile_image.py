# Generated by Django 4.2.6 on 2024-07-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0023_profile_user_prenom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='Profile'),
        ),
    ]
