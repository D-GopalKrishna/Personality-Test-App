# Generated by Django 3.1.6 on 2021-02-18 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0028_delete_userchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userselection',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Test.userdata', unique=True),
        ),
    ]
