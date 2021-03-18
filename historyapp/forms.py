from django import forms
from .models import HistoryImage
from .models import History
from django.core.files.uploadedfile import SimpleUploadedFile
class Insertform(forms.ModelForm):
    # bs1 = forms.IntegerField(max_value='20', min_value='-5')
    # bs2 = forms.IntegerField(max_value='20', min_value='-5')
    # bs3 = forms.IntegerField(max_value='20', min_value='-5')
    # bs4 = forms.IntegerField(max_value='20', min_value='-5')
    # bs5 = forms.IntegerField(max_value='20', min_value='-5')
    # bs6 = forms.IntegerField(max_value='20', min_value='-5')
    class Meta:
        model = History
        fields = ('bs1', 'bs2', 'bs3', 'bs4', 'bs5', 'bs6')
class UploadModelFrom(forms.ModelForm):
    
    class Meta:
        model = HistoryImage
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
