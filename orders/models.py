from django.db import models
from users.models import UserProfile
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.user_profile.user.username} - {self.product.name} x {self.quantity}"

class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'در انتظار پرداخت'),
        ('paid', 'پرداخت‌شده'),
        ('shipped', 'ارسال‌شده'),
        ('cancelled', 'لغو شده'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user_profile.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
