from django.db import models
from django.conf import settings
from services.models import Service

class Order(models.Model):
    CONSULTATION_CHOICES = [
        ('online', 'En ligne (Visioconférence sécurisée)'),
        ('in_person', 'En cabinet (Paris)'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name="Adresse", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="Ville", blank=True, null=True)
    postal_code = models.CharField(max_length=20, verbose_name="Code postal", blank=True, null=True)
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_CHOICES, default='in_person', verbose_name="Type de consultation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
