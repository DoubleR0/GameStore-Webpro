# Generated by Django 3.0.4 on 2020-03-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameLibrary', '0002_auto_20200310_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game_type',
            name='type_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
