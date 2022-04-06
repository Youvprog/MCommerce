from itertools import product
from django.db import models
from userlog.models import Customer
# Create your models here.


class Order(models.Model):
    song_name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    song_price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.song_name
    
    def total_price(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.TotalPrice for item in orderitems])
        return total

class OrderItem(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    song_name = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def TotalPrice(self):
        return self.quantity * self.song_name.song_price