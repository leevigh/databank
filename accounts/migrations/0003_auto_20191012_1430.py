# Generated by Django 2.1.4 on 2019-10-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191012_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(max_length=200, upload_to='files/cv'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
