import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

from django.db import models


class QRCode(models.Model):
    url = models.URLField(max_length=250)
    qr_code = models.ImageField(upload_to="Qr Codes", blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        qrcode_image = qrcode.make(self.url)
        create_image = Image.new('RGB', (335, 335), 'white')
        draw = ImageDraw.Draw(create_image)
        create_image.paste(qrcode_image)
        qr_name = f'qr_code_generator_.png'
        buffer = BytesIO()
        create_image.save(buffer, 'PNG')
        self.qr_code.save(qr_name, File(buffer), save=False)
        create_image.close()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.url
    