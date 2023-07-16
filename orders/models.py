from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    slug = models.SlugField(max_length=200, default='1')
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    """
        allow to store the course and price paid for 
        each of them
    """
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='join')
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    course = models.ForeignKey(Course,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price