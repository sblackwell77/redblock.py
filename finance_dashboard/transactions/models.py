from django.db import models

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.amount} ({self.category})"

# Add the Stock model to work with stock data
class Stock(models.Model):
    symbol = models.CharField(max_length=10)  # Stock symbol (e.g., AAPL for Apple)
    company_name = models.CharField(max_length=255)  # Company name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Stock price

    def __str__(self):
        return f"{self.company_name} ({self.symbol}) - ${self.price}"
