from django.db import models
from django.utils import timezone

class CalculatorOperation(models.Model):
    OPERATOR_CHOICES = [
        ('ADD', '+'),
        ('SUBTRACT', '-'),
        ('MULTIPLY', '*'),
        ('DIVIDE', '/'),
        ('POWER', '**'),
        ('SQRT', 'sqrt'),
        ('FACTORIAL', '!'),
        ('MODULUS', '%'),
        ('INT_DIVIDE', '//'),
    ]

    operator = models.CharField(max_length=10, choices=OPERATOR_CHOICES)
    first_number = models.FloatField()
    second_number = models.FloatField(null=True, blank=True)
    result = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_number} {self.get_operator_display()} {self.second_number} = {self.result} at {self.timestamp}"
