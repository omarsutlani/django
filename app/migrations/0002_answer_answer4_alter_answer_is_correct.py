# Generated by Django 4.2.4 on 2023-10-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer4',
            field=models.CharField(default='d', max_length=225),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.CharField(max_length=225),
        ),
    ]
