# Generated by Django 4.2.6 on 2024-07-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0009_annonces_user_alter_annonces_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonces',
            name='KG',
            field=models.IntegerField(),
        ),
    ]