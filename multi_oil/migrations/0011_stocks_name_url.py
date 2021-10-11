# Generated by Django 3.2.8 on 2021-10-09 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('multi_oil', '0010_alter_stocks_date_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='name_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
