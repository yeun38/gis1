# Generated by Django 3.2.4 on 2021-08-10 16:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conmment',
            new_name='Comment',
        ),
    ]