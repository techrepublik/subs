from django import forms
from .models import Region, Province, Municipality, Barangay
from accounts.models import User

class LocationForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
    province = forms.ModelChoiceField(queryset=Province.objects.none(), required=False)
    municipality = forms.ModelChoiceField(queryset=Municipality.objects.none(), required=False)
    barangay = forms.ModelChoiceField(queryset=Barangay.objects.none(), required=False)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"