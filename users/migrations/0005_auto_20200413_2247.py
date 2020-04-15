# Generated by Django 2.2.5 on 2020-04-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200413_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='supoerhost',
            new_name='superhost',
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], max_length=3, null=True),
        ),
    ]
