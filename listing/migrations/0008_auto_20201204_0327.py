# Generated by Django 3.1.2 on 2020-12-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_auto_20201204_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sub_category',
            field=models.CharField(choices=[('Phones', 'Phones'), ('Tablets', 'Tablets'), ('Cars', 'Cars'), ('Motorbikes', 'Motorbikes')], default='empty', max_length=255),
        ),
    ]
