# Generated by Django 3.1.5 on 2021-02-15 05:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0021_userselection_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='url_key',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]