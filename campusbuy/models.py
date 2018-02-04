from django.db import models
from django.utils import timezone


class ItemAdvert(models.Model):
    Seller_Name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Item = models.CharField(max_length= 200)
    Description = models.TextField()
    Asking_Price = models.FloatField()
    Created_data = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Item



# Create your models here.
