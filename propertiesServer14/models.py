from django.db import models

class property(models.Model):
    SALE='Sale'
    RENTEL="Rentel"
    PROPERTY_TYPE_CHOICES=[(SALE,'For Sale'),(RENTEL,'For Rentel'),]
    Name = models.CharField(max_length=100, blank=True, null=True)
    Rate = models.FloatField(blank=True, null=True)
    Location = models.CharField(max_length=20, blank=True, null=True)
    Squarefeet = models.CharField(max_length=10, blank=True, null=True)
    NoofBeds = models.IntegerField(blank=True, null=True)
    NoofBathrooms = models.IntegerField(blank=True, null=True)
    Facing = models.CharField(max_length=20, blank=True, null=True)
    Description = models.CharField(max_length=200, blank=True, null=True)
    Video=models.FileField(upload_to="videos",default=None,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.Name

class properyListdetails(models.Model):
    Listdetail = models.CharField(max_length=100, blank=True, null=True)
    PropImage=models.ImageField(upload_to="images",default=None,blank=True, null=True)
    propertyrel = models.ForeignKey(property, on_delete=models.CASCADE, related_name='properyListdetails', blank=True, null=True)
    def __str__(self) -> str:
        return self.Listdetail