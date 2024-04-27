from django.db import models

class property(models.Model):
    SALE='Sale'
    RENTEL="Rentel"
    APPARTMENT = "appartment"
    PROPERTY_TYPE_CHOICES=[(SALE,'For Sale'),(RENTEL,'For Rentel'),]   
    PROPERTY_LIST_CHOICES = [
        ('appartment', 'Apartment'),
        ('villa', 'Villa'),
        ('home', 'Home'),
        ('office', 'Office'),
        ('building', 'Building'),
        ('township', 'Township'),
        ('shop', 'Shop'),
        ('garage', 'Garage'),
    ]
    
    Name = models.CharField(max_length=100, default=None, blank=True, null=True)
    Rate = models.CharField(max_length=20,default=None,blank=True, null=True)
    Location = models.CharField(max_length=20,default=None, blank=True, null=True)
    Squarefeet = models.CharField(max_length=10,default=None ,blank=True, null=True)
    NoofBeds = models.CharField(max_length=20, default=None ,blank=True, null=True)
    NoofBathrooms = models.CharField(max_length=20,default=None, blank=True, null=True)
    Facing = models.CharField(max_length=20,default=None, blank=True, null=True)
    Description = models.CharField(max_length=1000,default=None, blank=True, null=True)
    Video=models.FileField(upload_to="videos",default=None,blank=True,null=True)
    PropertyType = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default=SALE,blank=True,null=True)
    PropertyList = models.CharField(max_length=20, choices=PROPERTY_LIST_CHOICES,default=APPARTMENT,blank=True,null=True)
    issold = models.BooleanField(default=False,blank=True,null=True)
    
    
    def __str__(self) -> str:
        return self.Name

class properyListdetails(models.Model):
    Listdetail = models.CharField(max_length=100, blank=True, null=True)
    PropImage=models.ImageField(upload_to="images",default=None,blank=True, null=True)
    propertyrel = models.ForeignKey(property, on_delete=models.CASCADE, related_name='properyListdetails', blank=True, null=True)
    def __str__(self) -> str:
        if self.propertyrel:
            return f"{self.Listdetail} - {self.propertyrel.Name}"
        else:
            return self.Listdetail