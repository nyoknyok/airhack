# Generated by Django 2.0 on 2018-08-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20180802_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='password',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
