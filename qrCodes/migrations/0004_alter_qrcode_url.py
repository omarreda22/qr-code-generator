# Generated by Django 4.2.3 on 2023-07-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodes', '0003_alter_qrcode_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='url',
            field=models.URLField(max_length=250),
        ),
    ]