# Generated by Django 3.1.5 on 2021-02-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0014_auto_20210209_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchoice',
            name='question_number',
        ),
        migrations.AddField(
            model_name='userchoice',
            name='question_number',
            field=models.ManyToManyField(to='Test.Question', verbose_name='questions_number'),
        ),
    ]
