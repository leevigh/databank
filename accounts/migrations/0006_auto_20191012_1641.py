# Generated by Django 2.1.4 on 2019-10-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191012_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='certs',
            field=models.FileField(blank=True, default='', max_length=200, upload_to='certs/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, max_length=200, upload_to='cv/%Y/%m/%d'),
        ),
    ]