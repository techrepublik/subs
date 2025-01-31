from django.shortcuts import render
from django.http import JsonResponse
from .models import Province, Municipality, Barangay

from .forms import LocationForm


def location_view(request):
    form = LocationForm()
    return render(request, 'location.html', {'form': form})

def load_provinces(request):
    region_id = request.GET.get('region_id')
    provinces = Province.objects.filter(region_id=region_id).order_by('name')
    return JsonResponse({'provinces': list(provinces.values('id', 'name'))})

def load_municipalities(request):
    province_id = request.GET.get('province_id')
    municipalities = Municipality.objects.filter(province_id=province_id).order_by('name')
    return JsonResponse({'municipalities': list(municipalities.values('id', 'name'))})

def load_barangays(request):
    municipality_id = request.GET.get('municipality_id')
    barangays = Barangay.objects.filter(municipality_id=municipality_id).order_by('name')
    return JsonResponse({'barangays': list(barangays.values('id', 'name'))})
