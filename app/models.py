from django.db import models

class PetrolEntry(models.Model):
    BIKE_CHOICES = [
        ('platina', 'Platina'),
        ('splendor', 'Splendor'),
    ]

    date = models.DateField()
    bike = models.CharField(max_length=20, choices=BIKE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.bike} - ₹{self.amount}"
