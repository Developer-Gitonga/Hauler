# Generated by Django 4.0.5 on 2022-06-23 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movingdetails',
            name='luggage_size',
            field=models.IntegerField(choices=[(1, 'Bedsitter'), (2, '1 Bedroom'), (3, '2 Bedroom'), (4, '3 Bedroom'), (5, 'Small Office'), (6, 'Medium Office'), (8, 'Large Office')], default=0),
        ),
    ]