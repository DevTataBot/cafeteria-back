# Generated by Django 3.2.8 on 2021-10-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0013_auto_20211026_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listproduct',
            name='idProducto',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listproduct',
            name='idUsuario',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]