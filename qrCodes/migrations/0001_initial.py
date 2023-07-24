# Generated by Django 4.2.3 on 2023-07-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='Qr Codes')),
            ],
        ),
    ]
