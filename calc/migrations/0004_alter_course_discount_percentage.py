# Generated by Django 3.2.7 on 2021-09-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20210926_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discount_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]