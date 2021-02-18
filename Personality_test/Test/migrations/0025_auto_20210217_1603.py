# Generated by Django 3.1.5 on 2021-02-17 16:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0024_auto_20210217_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='url_key',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='username',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
