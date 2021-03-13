from django.db import models
import datetime
from cust.models import User

# Create your models here.

class Property(models.Model):
    def year_choices():
        return [(r,r) for r in range(1984, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year

    property_name = models.CharField(max_length=200,null=True,blank=True)
    place = models.CharField(max_length=200,null=True,blank=True)
    area = models.IntegerField()
    cost_per_sqft = models.DecimalField(max_digits=7, decimal_places=2)
    no_of_bedroom = models.IntegerField()
    no_of_bathroom = models.IntegerField()
    year_of_manufacture = models.IntegerField(default=1984)

    def __str__(self):
        return self.property_name

class BuyAProperty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    properties = models.ForeignKey(Property, on_delete=models.CASCADE,null=True,blank=True)
    date_now = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.properties.property_name
