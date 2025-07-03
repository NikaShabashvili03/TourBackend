from django.db import models
from django.conf import settings
from django.utils import timezone
from ..models import Tour
from accounts.models import User

class Order(models.Model):
    ordered_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)

    def calculate_price(self):
        return self.tour.price

    def save(self, *args, **kwargs):
        calculated_price = self.calculate_price()
        if calculated_price is not None:
            self.price = calculated_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.ordered_by.email} - Price: {self.price}"
