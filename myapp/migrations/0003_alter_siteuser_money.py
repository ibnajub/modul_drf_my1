# Generated by Django 4.2 on 2023-06-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_women'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='money',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
