from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='products')
    description = models.TextField()
    image1 = models.ImageField(upload_to='products/%Y/%m/%d')
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("main:detail", kwargs={"p_slug": self.slug})
