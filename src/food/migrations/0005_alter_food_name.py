# Generated by Django 3.2 on 2022-05-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_food_spiciness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=20, verbose_name='name'),
        ),
    ]
