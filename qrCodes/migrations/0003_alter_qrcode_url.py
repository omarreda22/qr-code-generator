# Generated by Django 4.2.3 on 2023-07-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodes', '0002_qrcode_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='url',
            field=models.CharField(max_length=250),
        ),
    ]