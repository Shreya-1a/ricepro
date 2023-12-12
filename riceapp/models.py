from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)  
    
class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
   
class Godown(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

class Sell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    sell_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

class Purchase(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE)
    purchase_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    purchase_cost = models.IntegerField()

    
