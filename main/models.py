from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class House(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images')
    desc = models.TextField()
    price = models.PositiveBigIntegerField()
    bedroom = models.CharField(default=1)
    bathroom = models.PositiveSmallIntegerField(default=1)
    area = models.DecimalField(max_digits=10,decimal_places=2)
    floor = models.PositiveSmallIntegerField(default=2)
    parking = models.PositiveSmallIntegerField(default=2)
    room = models.PositiveSmallIntegerField(default=2)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='houses')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title