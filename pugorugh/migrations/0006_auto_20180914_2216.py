# Generated by Django 2.1.1 on 2018-09-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0005_auto_20180914_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpref',
            name='age',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='size',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
