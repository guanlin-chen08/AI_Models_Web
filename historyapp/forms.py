from django import forms
from .models import HistoryImage
from django.core.files.uploadedfile import SimpleUploadedFile
class Insertform(forms.Form):
    bs1 = forms.IntegerField(max_value='100', min_value='-100')
    bs2 = forms.IntegerField(max_value='100', min_value='-100')
    bs3 = forms.IntegerField(max_value='100', min_value='-100')
    bs4 = forms.IntegerField(max_value='100', min_value='-100')
    bs5 = forms.IntegerField(max_value='100', min_value='-100')
    bs6 = forms.IntegerField(max_value='100', min_value='-100')
    image = forms.ImageField()

class UploadModelFrom(forms.ModelForm):
    
    class Meta:
        model = HistoryImage
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
