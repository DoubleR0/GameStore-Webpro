# Generated by Django 3.0.4 on 2020-03-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameLibrary', '0003_auto_20200310_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(upload_to='../static/ImageGame'),
        ),
    ]