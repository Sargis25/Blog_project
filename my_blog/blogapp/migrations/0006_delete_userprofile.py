# Generated by Django 3.1.3 on 2021-04-29 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]