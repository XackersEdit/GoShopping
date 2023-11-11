# from core.models import Region, Cities
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=14, default='')
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    shipping = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='items', on_delete=models.CASCADE)
    supply_ability = models.FloatField()
    supply_ability_unit = models.CharField(max_length=255, default='')
    supply_ability_length = models.CharField(max_length=255, default='')
    supply_period = models.CharField(max_length=255, default='')
    payment_method = models.CharField(max_length=255, default='')
    # regions = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    # cities = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url