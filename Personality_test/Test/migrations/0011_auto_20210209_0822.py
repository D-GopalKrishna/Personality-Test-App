# Generated by Django 3.1.5 on 2021-02-09 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0010_auto_20210209_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='username',
            old_name='usernam',
            new_name='username',
        ),
    ]
