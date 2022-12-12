from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Location

# Create your views here.


def location_list(request):
    context = {'location_list': Location.objects.all()}
    return render(request, "location_register/location_list.html", context)


def location_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = LocationForm()
        else:
            location = Location.objects.get(pk=id)
            form = LocationForm(instance=location)
        return render(request, "location_register/location_form.html", {'form': form})
    else:
        if id == 0:
            form = LocationForm(request.POST)
        else:
            location = Location.objects.get(pk=id)
            form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
        return redirect('/location/list')


def location_delete(request, id):
    location = Location.objects.get(pk=id)
    location.delete()
    return redirect('/location/list')
