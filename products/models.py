from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"

    def __str__(self):
        return self.category

class Products(models.Model):
    status_choices = (
        ("Available" , "Available"),
        ("Not Available" , "Not Available"),
    )
    product_name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=255)
    status = models.CharField(max_length=225, choices=status_choices)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Products"

    def __str__(self):
        return self.product_name