# Generated by Django 2.1.4 on 2019-10-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191012_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='disabilities',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
