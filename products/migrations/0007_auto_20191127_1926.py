# Generated by Django 2.2.7 on 2019-11-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191127_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
