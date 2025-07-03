from django.db import models
from . import Location
from django.utils import timezone

class Tour(models.Model):
    CATEGORY_CHOICES = [
        ('horses', 'Horses'),
        ('tour', 'Tour'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='transfer')

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Tour #{self.id}"


class TourLocation(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='locations'
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ('tour', 'order') 

    def __str__(self):
        return f"{self.tour} - {self.order}: {self.location.name}"
