from django.db import models
# Create your models here.

class Category(models.Model):
    Name=models.CharField(max_length=80)
    Desc=models.TextField(blank=True)
    
    class Meta:
        # verbose_name= ("Category")
        verbose_name_plural= "Categories"
        
    def __str__(self):
        return self.Name
    
class Product(models.Model):
    name=models.CharField(max_length=80)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url=models.URLField(blank=True)
    quantity=models.PositiveIntegerField(default=0)
    featured=models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural= "Products"

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return self.quantity > 0
    

