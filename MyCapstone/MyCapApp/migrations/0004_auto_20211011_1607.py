# Generated by Django 3.2.7 on 2021-10-11 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyCapApp', '0003_auto_20211008_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='housingdata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='housingdata',
            name='rent1YearAvg',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='housingdata',
            name='rent5YearAvg',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='housingdata',
            name='value1YearAvg',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='housingdata',
            name='value5YearAvg',
            field=models.IntegerField(),
        ),
    ]
