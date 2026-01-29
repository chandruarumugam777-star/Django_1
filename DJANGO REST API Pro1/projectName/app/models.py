from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()

    def _str_(self):
        return self.title