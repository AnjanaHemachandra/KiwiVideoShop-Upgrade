# Generated by Django 2.1.1 on 2018-09-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieManager', '0002_auto_20180928_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
