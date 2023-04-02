from django.shortcuts import render, get_object_or_404
from .models import Farm, Field

def farm(request, farm):
    fields = Field.objects.get(farm__name=farm)
    return render(request,'question3/farm.html',{'farm': farm, 'fields': fields})