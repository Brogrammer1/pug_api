# Generated by Django 2.1.1 on 2018-09-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0003_auto_20180914_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpref',
            name='age',
            field=models.CharField(choices=[('b', 'baby'), ('y', 'young'), ('a', 'adult'), ('s', 'senior')], max_length=8),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('u', 'unknown')], max_length=6),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='size',
            field=models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large'), ('xl', 'extra large')], max_length=8),
        ),
    ]
