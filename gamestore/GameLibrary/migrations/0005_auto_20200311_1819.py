# Generated by Django 3.0.4 on 2020-03-11 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GameLibrary', '0004_auto_20200310_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(upload_to='ImageGame'),
        ),
        migrations.AlterField(
            model_name='user_games',
            name='purchased_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user_games',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
