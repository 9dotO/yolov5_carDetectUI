from django.db import models

import os

from django.db import models
from django.utils.translation import gettext_lazy as _


class ImageModel(models.Model):
    region = models.CharField(max_length=50)
    image = models.ImageField(_("image"), upload_to='images')
    result_image = models.ImageField(_("Result Image"), blank=True, null=True)
    # total = models.IntegerField(default=0)
    # car = models.IntegerField(default=0)    
    # minibus = models.IntegerField(default=0)
    # truck = models.IntegerField(default=0)
    # trailer = models.IntegerField(default=0)
    # motorcycle = models.IntegerField(default=0)
    car_class = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(os.path.split(self.image.path)[-1])