# Generated by Django 4.2.6 on 2024-07-16 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0019_alter_annonces_date_voyage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annonces_vu',
            old_name='me',
            new_name='client',
        ),
    ]