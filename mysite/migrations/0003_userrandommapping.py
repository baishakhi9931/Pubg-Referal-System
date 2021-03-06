# Generated by Django 2.2 on 2020-06-27 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20200624_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRandomMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_text', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.RegisteredUser')),
            ],
        ),
    ]
