from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from shops import constants


class Shop(models.Model):
    name = models.CharField(
        max_length=256,
    )

    latitude = models.DecimalField(
        max_digits=17,
        decimal_places=15,
        validators=[
            MaxValueValidator(-7.289515),
            MinValueValidator(-11.640186)
        ],
    )

    longitude = models.DecimalField(
        max_digits=17,
        decimal_places=15,
        validators=[
            MaxValueValidator(8.575844),
            MinValueValidator(4.017699)
        ],
    )

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "type": "Feature",
            "properties": {
                "Shop Name": self.name,
                "Items": [i.name for i in self.items.all()],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(self.latitude),
                    float(self.longitude),
                ]
            }
        }


class Item(models.Model):
    name = models.CharField(
        max_length=256,
    )

    category = models.CharField(
        max_length=256,
        choices=constants.ItemCategory.choices(),
        default=constants.ItemCategory.MISCELLANEOUS,
    )

    def __str__(self):
        return self.name


class ShopItem(models.Model):
    shop = models.ForeignKey(
        'shops.Shop',
        on_delete=models.CASCADE,
    )

    item = models.OneToOneField(
        'shops.Item',
        on_delete=models.CASCADE,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    currency = models.CharField(
        max_length=16,
        choices=constants.Currency.choices(),
        default=constants.Currency.LD,
    )

    notes = models.CharField(
        max_length=32,
    )

    def __str__(self):
        return f'{self.shop} {self.item}'
