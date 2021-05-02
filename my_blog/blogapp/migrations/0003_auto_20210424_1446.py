# Generated by Django 3.1.3 on 2021-04-24 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_profileinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='username',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
