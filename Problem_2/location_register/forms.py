from django import forms
from .models import Location


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('locationname','departmentname','category','subcategory')
        labels = {
            'locationname':'Location Name',
            'departmentname':'department'
        }

    def __init__(self, *args, **kwargs):
        super(LocationForm,self).__init__(*args, **kwargs)

