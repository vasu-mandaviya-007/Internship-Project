from django.db import models
import uuid

class Products(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    discription = models.TextField()
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
class Variants(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='variants')
    variant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.variant_name} of {self.product.title}"
    
class Images(models.Model):
    variant = models.ForeignKey(Variants, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.product.title}"
    
