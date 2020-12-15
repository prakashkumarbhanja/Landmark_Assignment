from django.db import models

# Create your models here.
class CaseStudy(models.Model):
    item_id = models.IntegerField()
    territory = models.CharField(max_length=10)
    warehouse_stock = models.IntegerField()
    store_stock = models.IntegerField()
    transit_stock = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.territory