from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)  # Book title
    author = models.CharField(max_length=50)  # Book author
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price

    published_date = models.DateField()  # Publication date

    def _str_(self):
        return self.title  # Friendly string representation