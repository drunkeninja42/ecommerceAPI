from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 255)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length = 155)
    category = models.ForeignKey(Category , related_name = 'book' , on_delete = models.CASCADE)
    isbn = models.CharField(max_length = 15)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    status = models.BooleanField(default = True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length = 15)
    name = models.CharField(max_length = 100)
    Category = models.ForeignKey(Category , related_name = 'product' , on_delete = models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    status = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return '{} {}'.format(self.product_tag,self.name)
