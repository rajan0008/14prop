from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from propertiesServer14.forms import PropertyListDetailForm
from .models import property, properyListdetails
# Create your views here.

def home(request):
    a = property.objects.all()
                       
    return render(request, "Base.html" , {"a": a})
def about(request):
                             
    return render(request, "about.html")
def contact(request):
                             
    return render(request, "contact.html")
def propertylist(request):
    a = property.objects.all()
                             
    return render(request, "propertylist.html",{"a": a})
def propertyagent(request):
                             
    return render(request, "propertyagent.html")
def propertytype(request):
                             
    return render(request, "propertytype.html")
def testimonial(request):
                             
    return render(request, "testimonial.html")
def viewprops(request):
    
    
    return render(request, "propertylist.html")
def viewpropdetails(request, id, Location, Facing, Rate):
    
    a = property.objects.get(id=id)
    
    return render(request, "propertydetails.html", {"a": a})