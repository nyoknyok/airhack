# Generated by Django 2.0 on 2018-08-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='airforce_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='area',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='carrer',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='classes',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='education',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='gender',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='interests',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
