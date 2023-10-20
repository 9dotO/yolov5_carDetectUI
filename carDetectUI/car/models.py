from django.db import models

import os

from django.db import models
from django.utils.translation import gettext_lazy as _


class ImageModel(models.Model):
    region = models.CharField(max_length=50)
    image = models.ImageField(_("image"), upload_to='images')
<<<<<<< HEAD
    result_image = models.ImageField(_("Result Image"), upload_to='results', blank=True, null=True)
    
    detected_classes = models.JSONField(null=True, blank=True)
    class_counts = models.JSONField(null=True, blank=True)
    
=======
    result_image = models.ImageField(_("Result Image"), blank=True, null=True)
    # total = models.IntegerField(default=0)
    # car = models.IntegerField(default=0)    
    # minibus = models.IntegerField(default=0)
    # truck = models.IntegerField(default=0)
    # trailer = models.IntegerField(default=0)
    # motorcycle = models.IntegerField(default=0)
    car_class = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

>>>>>>> ce6a1db9b4c6de70dc54f7bc21d6d4f592f2e9af
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
<<<<<<< HEAD
        return str(os.path.split(self.image.path)[-1])
    


    

class VideoModel(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')


    
=======
        return str(os.path.split(self.image.path)[-1])
>>>>>>> ce6a1db9b4c6de70dc54f7bc21d6d4f592f2e9af
