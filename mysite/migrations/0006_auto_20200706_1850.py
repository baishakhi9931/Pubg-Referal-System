# Generated by Django 2.2 on 2020-07-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200706_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='score',
        ),
        migrations.AlterField(
            model_name='completeduser',
            name='coins',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='completeduser',
            name='coins_sent',
            field=models.BooleanField(default=False),
        ),
    ]
