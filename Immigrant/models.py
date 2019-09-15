from django.db import models

# Create your models here.
class Culture(models.Model):
    country_name = models.CharField(max_length=100)
    country_info = models.TextField()
    country_info1 = models.TextField()
    country_info2 = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name

class Region(models.Model):
    region_name = models.CharField(max_length=50)
    migrant_num = models.IntegerField(default=0)
    country_name = models.ForeignKey(Culture, on_delete=models.DO_NOTHING)
    year = models.IntegerField(default=1996)

    def __str__(self):
        return "<Region: %s  Migrant: %s>" % (self.region_name, self.migrant_num)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=300)
   # location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #owner = models.CharField(max_length=50)


    def __str__(self):
        return "<Event: %s>" % self.title