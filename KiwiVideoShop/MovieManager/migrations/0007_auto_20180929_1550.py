# Generated by Django 2.1.1 on 2018-09-29 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieManager', '0006_movieinstance_renter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set Movie As Returned'),)},
        ),
    ]
