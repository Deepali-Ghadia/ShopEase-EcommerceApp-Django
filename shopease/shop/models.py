from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    
    # as of now, when I go to admin panel the product is displayed as Product object (1), Product object (2) but I want that proper name of object should be displayed on (http://127.0.0.1:8000/admin/shop/product/)
    # Therefore I will define a str method that returns product name
    
    def __str__(self):
        return self.product_name