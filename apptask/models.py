from django.db import models
from django.utils import timezone

class Record(models.Model):
    title = models.CharField(max_length=200)
    site = models.ForeignKey("Site")    
    created_date = models.DateField(
            default=timezone.now)
    a_record = models.DecimalField(max_digits=10, decimal_places=2)
    b_record = models.DecimalField(max_digits=10, decimal_places=2)

    def __repr__(self):
        return (self.site,self.created_date,self.a_record,self.b_record)

class Site(models.Model):
	site_name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.site_name)