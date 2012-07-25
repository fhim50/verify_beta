from django.db import models
from django.contrib import admin

class Product(models.Model):
	product_name = models.CharField(max_length=60)
	FDB_number = models.CharField(max_length=15,blank=True)
	manu_location = models.CharField(max_length=100,blank=True)
	strength = models.CharField(max_length=30,blank=True)
	dosage_form = models.CharField(max_length=30,blank=True)
	local_agent = models.CharField(max_length=100,blank=True)
	expiry_date = models.DateField(blank=True)
	
	
	def __unicode__(self):
		return self.product_name

admin.site.register(Product)

